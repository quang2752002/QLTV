package com.example.QLTV.model;


import jakarta.persistence.*;

@Entity
@Table(name = "Author")
public class Author {


    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(name = "Name", nullable = false, length = 100)
    private String name;

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

    public Boolean getState() {
        return state;
    }

    public void setState(Boolean state) {
        this.state = state;
    }
}