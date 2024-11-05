package com.example.QLTV.model;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;

@Entity


public class Category {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private int Id;
    private String Name;
    private String Description;
    private boolean State;
    public Category() {}
    public Category(int Id, String Name, String Description, boolean State) {
        this.Id = Id;
        this.Name = Name;
        this.Description = Description;
        this.State = State;
    }

    public boolean getState() {
        return State;
    }

    public void setState(boolean state) {
        State = state;
    }

    public String getDescription() {
        return Description;
    }

    public void setDescription(String description) {
        Description = description;
    }

    public String getName() {
        return Name;
    }

    public void setName(String name) {
        Name = name;
    }

    public int getId() {
        return Id;
    }

    public void setId(int id) {
        Id = id;
    }
}
