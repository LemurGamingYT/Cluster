#pragma once


/* 'mem' is a library for manually handling memory */


#include "../cluster.hpp"


struct PointerType {
    void* ptr;
};


#define Pointer PointerType


// func cast_param(0,void*)
inline Pointer point(void* memory) {
    Pointer p;
    p.ptr = memory;
    return p;
}

// func
inline nil_t malloc(Pointer p, int_t size) {
    p.ptr = malloc(size);
    return nil_t();
}

// func
inline nil_t realloc(Pointer p, int_t size) {
    p.ptr = realloc(p.ptr, size);
    return nil_t();
}

// func
inline nil_t Pointer_calloc(Pointer p, int_t size) {
    p.ptr = calloc(size, 1);
    return nil_t();
}


// property
inline int_t Pointer_sizeof(Pointer p) {
    return sizeof(p.ptr);
}

// method
inline nil_t Pointer_free(Pointer p) {
    delete p.ptr;
    return nil_t();
}
