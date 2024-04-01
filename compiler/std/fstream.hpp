#pragma once


/* 'fstream' is a library for handling files */


#include "../cluster.hpp"

#include <sys/stat.h>
#include <filesystem>
#include <fstream>


struct FileType {
    std::fstream file;
    std::filesystem::path p;
    string path;
};


#define File FileType


inline string_t type(File) { return "File"; }

inline string_t repr(File& f) { return "File(path=\"" + f.path + "\")"; }

inline bool_t tobool(File f) { return f.file.is_open(); }

// func
inline File open_file(string_t path) {
    File f;
    f.file.open(path);
    f.p = std::filesystem::path(path);
    f.path = path;
    return f;
}


// property
inline string_t File_path(File& f) { return f.path; }

// property
inline bool_t File_exists(File& f) { return std::filesystem::exists(f.p); }

// property
inline bool_t File_is_file(File& f) {
    return std::filesystem::is_regular_file(f.p);
}

// property
inline bool_t File_is_dir(File& f) {
    return std::filesystem::is_directory(f.p);
}

// property
inline string_t File_content(File& f) {
    if (!File_exists(f)) return "";

    std::ifstream t(f.path);
    t.seekg(0, std::ios::end);
    size_t size = t.tellg();
    string_t buf(size, ' ');
    t.seekg(0);
    t.read(&buf[0], size);
    return buf;
}

// property
inline arrayType<string_t> File_files(File& f) {
    if (!File_is_dir(f)) return arrayType<string_t>();

    arrayType<string_t> files;
    for (const auto& entry : std::filesystem::directory_iterator(f.path)) {
        files.elements.push_back(entry.path().filename().string());
    }
    return files;
}

// property
inline int_t File_size(File& f) {
    if (!File_exists(f)) return -1;
    if (!File_is_file(f)) return -1;

    return std::filesystem::file_size(f.p);
}

// method
inline nil_t File_close(File& f) {
    f.file.close();
    return nil_t();
}

// method
inline bool_t File_write(File& f, string_t s) {
    if (!File_exists(f)) return false;

    f.file << s;
    return true;
}

// method
inline bool_t File_delete(File& f) {
    f.file.close();
    return std::filesystem::remove(f.p);
}

// method
inline bool_t File_rename(File& f, string_t new_path) {
    try {
        std::filesystem::rename(f.p, std::filesystem::path(new_path));
        f.path = new_path;
        return true;
    } catch (const std::filesystem::filesystem_error& e) {
        return false;
    }
}

// method
inline bool_t File_move(File& f, string_t new_path) {
    try {
        std::filesystem::rename(f.p, std::filesystem::path(new_path));
        f.path = new_path;
        return true;
    } catch (const std::filesystem::filesystem_error& e) {
        return false;
    }
}

// method
inline nil_t File_create(File& f) {
    if (File_exists(f)) return nil_t();

    f.file.close();
    f.file.open(f.path, std::ios::out);

    return nil_t();
}
