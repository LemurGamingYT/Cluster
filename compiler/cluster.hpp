#pragma once

#include <filesystem>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>


using namespace std;


const string CLUSTER_VERSION = "0.0.2";

void err(string errType, string errMsg) {
    throw runtime_error(errType + ": " + errMsg);
}

#ifdef __unix__
    #define OS_UNIX
    #include <unistd.h>
#elif defined(_WIN32) || defined(WIN32)
    #define OS_WINDOWS
    #ifndef WIN32_LEAN_AND_MEAN
        #define WIN32_LEAN_AND_MEAN
    #endif

    #ifndef NOMINMAX
        #define NOMINMAX
    #endif

    #include <Windows.h>
#else
    #define OS_UNKNOWN
#endif


// types: Math, System, cluster

struct MathType{};
struct SystemType{};
struct clusterType{};


/*idea to implement dynamically typed arrays

in the Python compiler, keep track of every type of every element in every array
add special cases for the array attributes in the compiler like 'add' and 'get'

add implementation in the compiler
compiler.arrays.append(elementType)

get implementation in the compiler
compiler.arrays.get(elementType, index)
cast the result to the correct type*/


template <typename T>
struct arrayType {
    vector<T> elements;
};


#define int_t long long
#define float_t double
#define string_t string
#define bool_t bool
#define nil_t nullptr_t

#define Math MathType{}
#define System SystemType{}
#define cluster clusterType{}
#define hex_t unsigned long // Equivalent to DWORD from the Windows.h library


inline string_t type(int_t) { return "int"; }
inline string_t type(float_t) { return "float"; }
inline string_t type(string_t) { return "string"; }
inline string_t type(bool_t) { return "bool"; }
inline string_t type(nil_t) { return "nil"; }
inline string_t type(MathType) { return "Math"; }
inline string_t type(SystemType) { return "System"; }
template <typename T>
inline string_t type(arrayType<T>) { return "array[" + type(T()) + "]"; }
inline string_t type(clusterType) { return "cluster"; }
inline string_t type(hex_t) { return "hex"; }

inline string_t repr(int_t i) { return to_string(i); }
inline string_t repr(float_t f) { return to_string(f); }
inline string_t repr(string_t s) { return s; }
inline string_t repr(string_t s, bool_t) { return "'" + s + "'"; }
inline string_t repr(bool_t b) { return b ? "true" : "false"; }
inline string_t repr(nil_t) { return "nil"; }
inline string_t repr(hex_t h) { return "0x" + to_string(h); }

inline string_t repr(MathType) { return "class 'Math'"; }
inline string_t repr(SystemType) { return "class 'System'"; }
inline string_t repr(clusterType) { return "class 'cluster'"; }

template <typename T>
inline string_t repr(arrayType<T> a) {
    string_t res = "{";
    for (int_t i = 0; i < a.elements.size(); i++) {
        if (type(a.elements[i]) == "string") res += "'" + repr(a.elements[i]) + "'";
        else res += repr(a.elements[i]);
        if (i < a.elements.size() - 1) res += ", ";
    }
    res += "}";
    return res;
}


inline bool_t tobool(int_t i) { return i > 0; }
inline bool_t tobool(float_t f) { return f > 0.0; }
inline bool_t tobool(bool_t b) { return b; }
inline bool_t tobool(string_t s) { return !s.empty(); }
inline bool_t tobool(nil_t) { return false; }
inline bool_t tobool(hex_t h) { return h > 0; }

inline bool_t tobool(MathType) { return false; }
inline bool_t tobool(SystemType) { return false; }
inline bool_t tobool(clusterType) { return false; }

template <typename T>
inline bool_t tobool(arrayType<T> a) { return a.elements.size() > 0; }

inline nil_t print(string_t s) { cout << s << '\n'; return nil_t(); }
inline string_t input(string_t prompt) { cout << prompt; string_t res; cin >> res; return res; }

inline arrayType<int_t> range(int_t start, int_t end) {
    arrayType<int_t> res;
    for (int_t i = start; i < end; i++) res.elements.push_back(i);
    return res;
}

inline arrayType<int_t> range(int_t end) {
    arrayType<int_t> res;
    for (int_t i = 0; i < end; i++) res.elements.push_back(i);
    return res;
}

inline arrayType<int_t> range(int_t start, int_t end, int_t step) {
    arrayType<int_t> res;
    for (int_t i = start; i < end; i += step) res.elements.push_back(i);
    return res;
}


inline int_t add(int_t a, int_t b) { return a + b; }
inline float_t add(float_t a, float_t b) { return a + b; }
inline string_t add(string_t a, string_t b) { return a + b; }
template <typename T>
inline arrayType<T> add(arrayType<T> a, T b) { a.elements.push_back(b); return a; }
template <typename T>
inline arrayType<T> add(arrayType<T> a, arrayType<T> b) {
    a.elements.insert(a.elements.end(), b.elements.begin(), b.elements.end());
    return a;
}

inline int_t sub(int_t a, int_t b) { return a - b; }
inline float_t sub(float_t a, float_t b) { return a - b; }
inline string_t sub(string_t a, int_t b) { return a.substr(0, a.length() - b); }

inline int_t mul(int_t a, int_t b) { return a * b; }
inline float_t mul(float_t a, float_t b) { return a * b; }
inline string_t mul(string_t a, int_t b) {
    string_t res = "";
    for (int_t i = 0; i < b; i++) res += a;
    return res;
}

inline int_t div_(int_t a, int_t b) { return a / b; }
inline float_t div_(float_t a, float_t b) { return a / b; }
inline string_t div_(string_t a, int_t b) { return a.substr(b); }

inline int_t mod(int_t a, int_t b) { return a % b; }
inline string_t mod(int_t a, string_t b) {
    string_t res = "";
    for (int_t i = 0; i < a; i++) {
        res += b[i];
    }

    return res;
}
inline string_t mod(string_t a, int_t b) {
    string_t res = "";
    for (int_t i = b; i > 0; i--) {
        res += a[i];
    }

    return res;
}

inline bool_t eq(int_t a, int_t b) { return a == b; }
inline bool_t eq(float_t a, float_t b) { return a == b; }
inline bool_t eq(string_t a, string_t b) { return a == b; }
inline bool_t eq(bool_t a, bool_t b) { return a == b; }
inline bool_t eq(nil_t, nil_t) { return true; }
template <typename T>
inline bool_t eq(arrayType<T> a, arrayType<T> b) { return a.elements == b.elements; }

inline bool_t neq(int_t a, int_t b) { return a != b; }
inline bool_t neq(float_t a, float_t b) { return a != b; }
inline bool_t neq(string_t a, string_t b) { return a != b; }
inline bool_t neq(bool_t a, bool_t b) { return a != b; }
inline bool_t neq(nil_t, nil_t) { return false; }
template <typename T>
inline bool_t neq(arrayType<T> a, arrayType<T> b) { return a.elements != b.elements; }

inline bool_t gt(int_t a, int_t b) { return a > b; }
inline bool_t gt(float_t a, float_t b) { return a > b; }
inline bool_t gt(string_t a, string_t b) { return a.length() > b.length(); }
template <typename T>
inline bool_t gt(arrayType<T> a, arrayType<T> b) { return a.elements.size() > b.elements.size(); }

inline bool_t gte(int_t a, int_t b) { return a >= b; }
inline bool_t gte(float_t a, float_t b) { return a >= b; }
inline bool_t gte(string_t a, string_t b) { return a.length() >= b.length(); }
template <typename T>
inline bool_t gte(arrayType<T> a, arrayType<T> b) { return a.elements.size() >= b.elements.size(); }

inline bool_t lt(int_t a, int_t b) { return a < b; }
inline bool_t lt(float_t a, float_t b) { return a < b; }
inline bool_t lt(string_t a, string_t b) { return a.length() < b.length(); }
template <typename T>
inline bool_t lt(arrayType<T> a, arrayType<T> b) { return a.elements.size() < b.elements.size(); }

inline bool_t lte(int_t a, int_t b) { return a <= b; }
inline bool_t lte(float_t a, float_t b) { return a <= b; }
inline bool_t lte(string_t a, string_t b) { return a.length() <= b.length(); }
template <typename T>
inline bool_t lte(arrayType<T> a, arrayType<T> b) { return a.elements.size() <= b.elements.size(); }

inline bool_t and_(bool_t a, bool_t b) { return a && b; }

inline bool_t or_(bool_t a, bool_t b) { return a || b; }

inline bool_t not_(bool_t a) { return !a; }
inline string_t not_(string_t a) {
    string_t res = a;
    reverse(res.begin(), res.end());
    return res;
}


// property
inline int_t string_length(string_t s) { return s.length(); }

// property
inline string_t string_start(string_t s) { return s.substr(0, 1); }

// property
inline string_t string_end(string_t s) { return s.substr(s.length() - 1); }

// method
inline int_t string_parse_int(string_t s) {
    return stoll(s);
}

// method
inline float_t string_parse_float(string_t s) {
    return stof(s);
}

// method
inline bool_t string_parse_bool(string_t s) {
    return s == "true";
}

// method
inline bool_t string_is_digit(string_t s) {
    return all_of(s.begin(), s.end(), ::isdigit);
}

// method
inline bool_t string_is_decimal(string_t s) {
    return all_of(s.begin(), s.end(), ::isdigit) || s == ".";
}

// method
inline bool_t string_is_lower(string_t s) {
    return all_of(s.begin(), s.end(), ::islower);
}

// method
inline bool_t string_is_upper(string_t s) {
    return all_of(s.begin(), s.end(), ::isupper);
}

// method
inline bool_t string_is_alphanum(string_t s) {
    return all_of(s.begin(), s.end(), ::isalnum);
}

// method
inline bool_t string_is_alpha(string_t s) {
    return all_of(s.begin(), s.end(), ::isalpha);
}

// method
inline bool_t string_is_whitespace(string_t s) {
    return all_of(s.begin(), s.end(), ::isspace);
}

// method
inline bool_t string_is_printable(string_t s) {
    return all_of(s.begin(), s.end(), ::isprint);
}

// method
inline string_t string_lower(string_t s) {
    string_t res = s;
    transform(res.begin(), res.end(), res.begin(), ::tolower);
    return res;
}

// method
inline string_t string_upper(string_t s) {
    string_t res = s;
    transform(res.begin(), res.end(), res.begin(), ::toupper);
    return res;
}

// method
inline arrayType<string_t> string_split(string_t s, string_t delimiter) {
    arrayType<string_t> res;
    size_t pos = 0;
    string_t token;
    while ((pos = s.find(delimiter)) != string::npos) {
        token = s.substr(0, pos);
        res.elements.push_back(token);
        s.erase(0, pos + delimiter.length());
    }
    res.elements.push_back(s);
    return res;
}

// method
inline string_t string_join(string_t s, arrayType<string_t> elements) {
    string_t res;
    for (int_t i = 0; i < elements.elements.size(); i++) {
        res += elements.elements[i];
        if (i < elements.elements.size() - 1) res += s;
    }

    return res;
}


template <typename T>
arrayType<T> new_array(vector<T> elements) {
    arrayType<T> a;
    a.elements = elements;
    return a;
}

template <typename T>
// property
inline int_t array_length(arrayType<T> a) {
    return a.elements.size();
}

template <typename T>
// method
inline nil_t array_add(arrayType<T>& a, T element) {
    a.elements.push_back(element);
    return nil_t();
}

template <typename T>
// method
inline nil_t array_insert(arrayType<T>& a, int_t index, T element) {
    a.elements.insert(a.elements.begin() + index, element);
    return nil_t();
}

template <typename T>
// method
inline nil_t array_remove(arrayType<T>& a, int_t index) {
    a.elements.erase(a.elements.begin() + index);
    return nil_t();
}

template <typename T>
// method
inline nil_t array_clear(arrayType<T>& a) {
    a.elements.clear();
    return nil_t();
}

template <typename T>
// method
inline T array_pop(arrayType<T>& a) {
    a.elements.pop_back();
    return a.elements.back();
}

template <typename T>
// method
inline T array_pop(arrayType<T>& a, int_t index) {
    T res = a.elements[index];
    a.elements.erase(a.elements.begin() + index);
    return res;
}

template <typename T>
// method
inline nil_t array_set(arrayType<T>& a, int_t index, T element) {
    a.elements[index] = element;
    return nil_t();
}

template <typename T>
// method
inline T array_get(arrayType<T> a, int_t index) {
    if (a.elements.size() <= index) {
        err("Range", "Index out of range " + repr(index));
    }

    return a.elements[index];
}

template <typename T>
// method
inline bool_t array_has(arrayType<T> a, T element) {
    return find(a.elements.begin(), a.elements.end(), element) != a.elements.end();
}

template <typename T>
// method
inline nil_t array_sort(arrayType<T>& a) {
    sort(a.elements.begin(), a.elements.end());
    return nil_t();
}

template <typename T>
// method
inline bool_t array_is_sorted(arrayType<T> a) {
    return is_sorted(a.elements.begin(), a.elements.end());
}

template <typename T>
// method
inline bool_t array_any(arrayType<T> a) {
    return any_of(a.elements.begin(), a.elements.end(), [](T x) { return tobool(x); });
}

template <typename T>
// method
inline bool_t array_all(arrayType<T> a) {
    return all_of(a.elements.begin(), a.elements.end(), [](T x) { return tobool(x); });
}


// property static
inline float_t Math_pi() { return 3.14159265358979323846; }

// property static
inline float_t Math_e() { return 2.71828182845904523536; }

// method static
inline float_t Math_sin(float_t x) { return sin(x); }

// method static
inline float_t Math_cos(float_t x) {
    return cos(x);
}

// method static
inline float_t Math_tan(float_t x) {
    return tan(x);
}

// method static
inline float_t Math_log(float_t x) {
    return log(x);
}

// method static
inline float_t Math_log10(float_t x) {
    return log10(x);
}

// method static
inline float_t Math_pow(float_t x, float_t y) {
    return pow(x, y);
}

// method static
inline float_t Math_sqrt(float_t x) {
    return sqrt(x);
}

// method static
inline float_t Math_abs(float_t x) {
    return abs(x);
}

// method static
inline float_t Math_round(float_t x) {
    return round(x);
}

// method static
inline float_t Math_floor(float_t x) {
    return floor(x);
}

// method static
inline float_t Math_ceil(float_t x) {
    return ceil(x);
}

// method static
inline float_t Math_deg(float_t x) {
    return x * 180.0 / Math_pi();
}

// method static
inline float_t Math_rad(float_t x) {
    return x * Math_pi() / 180.0;
}

// method static
inline float_t Math_atan2(float_t y, float_t x) {
    return atan2(y, x);
}

// method static
inline float_t Math_acos(float_t x) {
    return acos(x);
}

// method static
inline float_t Math_asin(float_t x) {
    return asin(x);
}

// method static
inline float_t Math_hypot(float_t x, float_t y) {
    return hypot(x, y);
}

// method static
inline float_t Math_atan(float_t x) {
    return atan(x);
}

// method static
inline int_t Math_min(int_t a, int_t b) {
    return min(a, b);
}

// method static
inline float_t Math_min(float_t a, float_t b) {
    return min(a, b);
}

// method static
inline int_t Math_max(int_t a, int_t b) {
    return max(a, b);
}

// method static
inline float_t Math_max(float_t a, float_t b) {
    return max(a, b);
}


// property static
inline string_t System_cd() {
    filesystem::path currentDir = filesystem::current_path();
    return currentDir.string();
}

// property static
inline int_t System_pid() {
#ifdef OS_WINDOWS
    return GetCurrentProcessId();
#endif

#ifdef OS_UNIX
    return getpid();
#endif

    return -1;
}

// method static
inline nil_t System_exit(int_t code) {
    exit(code);
}

// method static
inline nil_t System_exit() {
    exit(0);
}

// method static
inline int_t System_shell(string_t command) {
    return (int_t)system(command.c_str());
}

// method static
inline nil_t System_mouse_to(int_t x, int_t y) {
#ifdef OS_WINDOWS
    SetCursorPos(x, y);
#else
    err("Sys", "System.mouse_to() is not supported for this OS");
#endif

    return nil_t();
}

// method static
inline nil_t System_key_press(string_t key) {
#ifdef OS_WINDOWS
    keybd_event(key[0], 0, 0, 0);
#else
    err("Sys", "System.key_press() is not supported for this OS");
#endif

    return nil_t();
}

// method static
inline nil_t System_key_up(string_t key) {
#ifdef OS_WINDOWS
    keybd_event(key[0], 0, KEYEVENTF_KEYUP, 0);
#else
    err("Sys", "System.key_up() is not supported for this OS");
#endif

    return nil_t();
}


// property static
inline string_t cluster_version() {
    return CLUSTER_VERSION;
}
