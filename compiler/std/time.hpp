#pragma once


/* 'time' is a library for time related functions */


#include "../cluster.hpp"

#include <chrono>
#include <thread>


// func
inline nil_t sleep(int_t ms) {
    std::this_thread::sleep_for(std::chrono::milliseconds(ms));
    return nil_t();
}

// func
inline string_t current_time() {
    time_t now = time(0);
    struct tm tstruct;
    char buf[80];
    tstruct = *localtime(&now);
    strftime(buf, sizeof(buf), "%X", &tstruct);
    return string_t(buf);
}

// func
inline float_t time_now() {
    return time(0);
}
