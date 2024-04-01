/*#pragma once


#include "./include/HTTPRequest.hpp"
#include "../cluster.hpp"


typedef struct {
    http::Response response;
    string url;
} ResponseType;


#define Response ResponseType


inline string_t type(ResponseType) { return "Response"; }

inline string_t repr(ResponseType r) { return "Response(url=\"" + r.url + "\""; }

inline bool_t tobool(ResponseType r) { return r.response.status.code == 200; }


// func
inline bool_t knock(string_t url) {
    try {
        http::Request req{url};
        const auto response = req.send("GET");
        return true;
    } catch (const std::exception& e) {
        err("HTTP", "Request failed, error: " + string(e.what()));
    }
}


// property
inline int_t Response_status(ResponseType r) { return (int_t) r.response.status.code; }

// property
inline string_t Response_url(ResponseType r) { return r.url; }*/
