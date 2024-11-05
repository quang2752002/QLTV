package com.example.QLTV.model;

import jakarta.persistence.*;
import lombok.Data;

@Entity
@Data
@Table(name="Book")
public class Book {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(name = "AuthorId", nullable = false)
    private Integer authorId;

    @Column(name = "CategoryId", nullable = false)
    private Integer categoryId;

    @ManyToOne
    @JoinColumn(name = "AuthorId", referencedColumnName = "Id", insertable = false, updatable = false)
    private Author author;

    @ManyToOne
    @JoinColumn(name = "CategoryId", referencedColumnName = "Id", insertable = false, updatable = false)
    private Category category;

    @Column(name = "Name", nullable = false)
    private String name;

    @Column(name = "ShelfRow")
    private Integer shelfRow;

    @Column(name = "ShelfCol")
    private Integer shelfCol;

    @Column(name = "Description")
    private String description;

    @Column(name = "State")
    private Boolean state;

    // Getters and Setters
    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public Integer getAuthorId() {
        return authorId;
    }

    public void setAuthorId(Integer authorId) {
        this.authorId = authorId;
    }

    public Integer getCategoryId() {
        return categoryId;
    }

    public void setCategoryId(Integer categoryId) {
        this.categoryId = categoryId;
    }

    public Author getAuthor() {
        return author;
    }

    public void setAuthor(Author author) {
        this.author = author;
    }

    public Category getCategory() {
        return category;
    }

    public void setCategory(Category category) {
        this.category = category;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Integer getShelfRow() {
        return shelfRow;
    }

    public void setShelfRow(Integer shelfRow) {
        this.shelfRow = shelfRow;
    }

    public Integer getShelfCol() {
        return shelfCol;
    }

    public void setShelfCol(Integer shelfCol) {
        this.shelfCol = shelfCol;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public Boolean getState() {
        return state;
    }

    public void setState(Boolean state) {
        this.state = state;
    }
}