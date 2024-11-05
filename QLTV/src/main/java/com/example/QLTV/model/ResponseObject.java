package com.example.QLTV.model;

import org.springframework.http.HttpStatus;

public class ResponseObject {
    private HttpStatus response; // Use HttpStatus instead of int
    private String message;
    private Object data;

    public ResponseObject() {
    }

    public ResponseObject(HttpStatus response, String message, Object data) {
        this.response = response;
        this.message = message;
        this.data = data;
    }

    public HttpStatus getResponse() {
        return response;
    }

    public void setResponse(HttpStatus response) {
        this.response = response;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public Object getData() {
        return data;
    }

    public void setData(Object data) {
        this.data = data;
    }
}
