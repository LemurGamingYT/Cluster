#pragma once

#include <algorithm>
#include <iostream>
#include <string>
#include <cmath>


using namespace std;


#define CLUSTER_VERSION "0.0.1"


typedef struct{} MathType;


#define int_t long long
#define float_t double
#define string_t string
#define bool_t bool
#define nil_t nullptr_t
#define Math MathType{}


inline string_t type(int_t) { return "int"; }
inline string_t type(float_t) { return "float"; }
inline string_t type(string_t) { return "string"; }
inline string_t type(bool_t) { return "bool"; }
inline string_t type(nil_t) { return "nil"; }
inline string_t type(MathType) { return "Math"; }

inline string_t repr(int_t i) { return to_string(i); }
inline string_t repr(float_t f) { return to_string(f); }
inline string_t repr(bool_t b) { return to_string(b); }
inline string_t repr(nil_t) { return "nil"; }
inline string_t repr(MathType) { return "class 'Math'"; }

inline bool_t tobool(int_t i) { return i > 0; }
inline bool_t tobool(float_t f) { return f > 0.0; }
inline bool_t tobool(bool_t b) { return b; }
inline bool_t tobool(string_t s) { return !s.empty(); }
inline bool_t tobool(nil_t) { return false; }
inline bool_t tobool(MathType) { return false; }


inline nil_t print(string_t s) { cout << s << '\n'; return nil_t(); }


inline int_t add(int_t a, int_t b) { return a + b; }
inline float_t add(float_t a, float_t b) { return a + b; }
inline string_t add(string_t a, string_t b) { return a + b; }

inline int_t sub(int_t a, int_t b) { return a - b; }
inline float_t sub(float_t a, float_t b) { return a - b; }

inline int_t mul(int_t a, int_t b) { return a * b; }
inline float_t mul(float_t a, float_t b) { return a * b; }

inline int_t div_(int_t a, int_t b) { return a / b; }

inline float_t div_(float_t a, float_t b) { return a / b; }

inline int_t mod(int_t a, int_t b) { return a % b; }

inline bool_t eq(int_t a, int_t b) { return a == b; }
inline bool_t eq(float_t a, float_t b) { return a == b; }
inline bool_t eq(string_t a, string_t b) { return a == b; }
inline bool_t eq(bool_t a, bool_t b) { return a == b; }
inline bool_t eq(nil_t, nil_t) { return true; }

inline bool_t neq(int_t a, int_t b) { return a != b; }
inline bool_t neq(float_t a, float_t b) { return a != b; }
inline bool_t neq(string_t a, string_t b) { return a != b; }
inline bool_t neq(bool_t a, bool_t b) { return a != b; }
inline bool_t neq(nil_t, nil_t) { return false; }

inline bool_t gt(int_t a, int_t b) { return a > b; }
inline bool_t gt(float_t a, float_t b) { return a > b; }
inline bool_t gt(string_t a, string_t b) { return a.length() > b.length(); }

inline bool_t gte(int_t a, int_t b) { return a >= b; }
inline bool_t gte(float_t a, float_t b) { return a >= b; }
inline bool_t gte(string_t a, string_t b) { return a.length() >= b.length(); }

inline bool_t lt(int_t a, int_t b) { return a < b; }
inline bool_t lt(float_t a, float_t b) { return a < b; }
inline bool_t lt(string_t a, string_t b) { return a.length() < b.length(); }

inline bool_t lte(int_t a, int_t b) { return a <= b; }
inline bool_t lte(float_t a, float_t b) { return a <= b; }
inline bool_t lte(string_t a, string_t b) { return a.length() <= b.length(); }

inline bool_t and_(bool_t a, bool_t b) { return a && b; }

inline bool_t or_(bool_t a, bool_t b) { return a || b; }

inline bool_t not_(bool_t a) { return !a; }


// property
inline int_t string_length(string_t s) { return s.length(); }

// property
inline string_t string_start(string_t s) { return s.substr(0, 1); }

// property
inline string_t string_end(string_t s) { return s.substr(s.length() - 1); }

// property
inline string_t string_reversed(string_t s) {
    string_t res = s;
    reverse(res.begin(), res.end());
    return res;
}

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
inline bool_t string_is_alphabetic(string_t s) {
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
