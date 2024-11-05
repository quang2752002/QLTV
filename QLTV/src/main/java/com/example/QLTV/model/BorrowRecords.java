package com.example.QLTV.model;

import jakarta.persistence.*;

import java.util.Date;

@Entity
@Table(name = "BorrowRecords")
public class BorrowRecords {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(name = "UserId", nullable = false)
    private Integer userId;

    @Column(name = "BookDetailId", nullable = false)
    private Integer bookDetailId;

    @ManyToOne
    @JoinColumn(name = "UserId", referencedColumnName = "Id", insertable = false, updatable = false)
    private User user;

    @ManyToOne
    @JoinColumn(name = "BookDetailId", referencedColumnName = "Id", insertable = false, updatable = false)
    private BookDetail bookDetail;

    @Column(name = "NgayMuon")
    private Date borrowDate;

    @Column(name = "HanTra")
    private Date dueDate;

    @Column(name = "NgayTra")
    private Date returnDate;

    @Column(name = "State")
    private Boolean state;

    // Getters and Setters
    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public Integer getUserId() {
        return userId;
    }

    public void setUserId(Integer userId) {
        this.userId = userId;
    }

    public Integer getBookDetailId() {
        return bookDetailId;
    }

    public void setBookDetailId(Integer bookDetailId) {
        this.bookDetailId = bookDetailId;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

    public BookDetail getBookDetail() {
        return bookDetail;
    }

    public void setBookDetail(BookDetail bookDetail) {
        this.bookDetail = bookDetail;
    }

    public Date getBorrowDate() {
        return borrowDate;
    }

    public void setBorrowDate(Date borrowDate) {
        this.borrowDate = borrowDate;
    }

    public Date getDueDate() {
        return dueDate;
    }

    public void setDueDate(Date dueDate) {
        this.dueDate = dueDate;
    }

    public Date getReturnDate() {
        return returnDate;
    }

    public void setReturnDate(Date returnDate) {
        this.returnDate = returnDate;
    }

    public Boolean getState() {
        return state;
    }

    public void setState(Boolean state) {
        this.state = state;
    }
}