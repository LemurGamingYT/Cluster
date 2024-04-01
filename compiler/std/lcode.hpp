#pragma once


/* 'lcode' is a library that contains functions for various leet code problems */


#include "../cluster.hpp"

#include <set>


// func
inline int_t reverse_int(int_t x) {
    int_t max_int = pow(2, 31) - 1;
    int_t min_int = pow(-2, 31);
    int_t reverse;

    while (x != 0) {
        if (reverse > max_int / 10 || reverse < min_int / 10) {
            return 0;
        }

        reverse = reverse * 10 + x % 10;
        x = trunc(x / 10);
    }

    return reverse;
}

// func
inline int_t length_of_longest_substring(string_t s) {
    int_t n = s.length();
    std::set<char> char_set = {};
    int_t max_length = 0;
    int_t left = 0;

    for (int_t right = 0; right < n; right++) {
        if (char_set.find(s[right]) != char_set.end()) {
            while (s[left] != s[right]) {
                char_set.erase(s[left]);
                left++;
            }
            char_set.erase(s[left]);
            left++;
        }
        char_set.insert(s[right]);
        max_length = max(max_length, right - left + 1);
    }

    return max_length;
}

// func
inline bool_t is_palindrome_int(int_t x) {
    if (x < 0) {
        return false;
    }

    int_t reversed_num = 0;
    int_t temp = x;
    while (temp != 0) {
        reversed_num = reversed_num * 10 + temp % 10;
        temp /= 10;
    }

    return reversed_num == x;
}

// func
inline bool_t is_parenthesis_valid(string_t s) {
    vector<char> stack = {};
    for (char c : s) {
        if (c == '(' || c == '[' || c == '{') {
            stack.push_back(c);
        } else if (c == ')' && !stack.empty() && stack.back() == '(') {
            stack.pop_back();
        } else if (c == ']' && !stack.empty() && stack.back() == '[') {
            stack.pop_back();
        } else if (c == '}' && !stack.empty() && stack.back() == '{') {
            stack.pop_back();
        } else {
            return false;
        }
    }

    return stack.empty();
}
