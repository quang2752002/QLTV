package com.example.QLTV.model;


import jakarta.persistence.*;

@Entity
@Table(name = "Img")
public class Img {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    private Integer bookId;

    private String url;

    private Boolean state;

    // Getters and Setters
    // ...
}
