package com.example.QLTV.model;

import jakarta.persistence.*;


@Entity
@Table(name = "BookDetail")
public class BookDetail {


    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(name = "BookId", nullable = false)
    private Integer bookId;

    @ManyToOne
    @JoinColumn(name = "BookId", referencedColumnName = "Id", insertable = false, updatable = false)
    private Book book;

    @Column(name = "Url", nullable = false, length = 255)
    private String url;

    @Column(name = "State")
    private Boolean state;

    // Getters and Setters
    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public Integer getBookId() {
        return bookId;
    }

    public void setBookId(Integer bookId) {
        this.bookId = bookId;
    }

    public Book getBook() {
        return book;
    }

    public void setBook(Book book) {
        this.book = book;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public Boolean getState() {
        return state;
    }

    public void setState(Boolean state) {
        this.state = state;
    }
}