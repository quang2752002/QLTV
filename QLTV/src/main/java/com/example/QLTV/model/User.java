package com.example.QLTV.model;

import jakarta.persistence.*;


import java.util.Date;

@Entity
@Table(name = "User")
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(name = "Name", length = 100)
    private String name;

    @Column(name = "SDT", length = 11)
    private String phoneNumber;

    @Column(name = "Address", length = 100)
    private String address;

    @Column(name = "Birthday")
    private java.util.Date birthday;

    @Column(name = "State")
    private Boolean state;

    // Getters and Setters
    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    public void setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public java.util.Date getBirthday() {
        return birthday;
    }

    public void setBirthday(java.util.Date birthday) {
        this.birthday = birthday;
    }

    public Boolean getState() {
        return state;
    }

    public void setState(Boolean state) {
        this.state = state;
    }
}