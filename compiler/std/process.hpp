#pragma once


/* 'process' is a library for manipulating processes */


#include "../cluster.hpp"


#ifndef OS_WINDOWS
    #error Unsupported OS for 'process' library
#endif


struct ProcessType {
    hex_t pid;
    HANDLE handle;
};

#define Process ProcessType


inline string_t type(ProcessType) { return "Process"; }

inline string_t repr(ProcessType p) { return "Process(pid=" + to_string(p.pid) + ")"; }

inline bool_t tobool(ProcessType p) { return p.pid && p.handle; }


// func
inline Process open_process(string_t name) {
    HWND hwnd = FindWindowA(NULL, name.c_str());
    if (hwnd == NULL) {
        return Process{(hex_t)NULL, (HANDLE)NULL};
    }

    hex_t pid;

    GetWindowThreadProcessId(hwnd, &pid);
    HANDLE handle = OpenProcess(PROCESS_ALL_ACCESS, FALSE, pid);
    return Process{pid, handle};
}

// func
inline Process open_process(int_t pid) {
    HANDLE handle = OpenProcess(PROCESS_ALL_ACCESS, FALSE, pid);
    return Process{(unsigned long)pid, handle};
}


// property
inline int_t Process_pid(Process p) { return p.pid; }

// method
inline nil_t Process_close(Process p) {
    CloseHandle(p.handle);
    return nil_t();
}

// method
inline nil_t Process_kill(Process p) {
    TerminateProcess(p.handle, 0);
    return nil_t();
}

// method
inline hex_t Process_read(Process p, hex_t pointerAddress) {
    hex_t pointerAddr = (hex_t) pointerAddress;
    if (!ReadProcessMemory(p.handle, (LPVOID)pointerAddr, &pointerAddr, sizeof(pointerAddr), NULL)) {
        err("Process", "Reading from process failed");
    }

    return (int_t) pointerAddr;
}

// method
inline bool_t Process_write(Process p, hex_t pointerAddress, int_t value) {
    hex_t pointerAddr = (hex_t) pointerAddress;
    if (!WriteProcessMemory(p.handle, (LPVOID)pointerAddr, &value, sizeof(value), NULL)) {
        return false;
    }

    return true;
}
