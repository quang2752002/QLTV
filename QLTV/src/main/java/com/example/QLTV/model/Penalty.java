package com.example.QLTV.model;

import jakarta.persistence.*;


@Entity
@Table(name = "Penalty")
public class Penalty {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(name = "BorrowRecordId", unique = true, nullable = false)
    private Integer borrowRecordId;

    @ManyToOne
    @JoinColumn(name = "BorrowRecordId", referencedColumnName = "Id", insertable = false, updatable = false)
    private BorrowRecords borrowRecords;

    @Column(name = "State")
    private Boolean state;

    // Getters and Setters
    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public Integer getBorrowRecordId() {
        return borrowRecordId;
    }

    public void setBorrowRecordId(Integer borrowRecordId) {
        this.borrowRecordId = borrowRecordId;
    }

    public BorrowRecords getBorrowRecords() {
        return borrowRecords;
    }

    public void setBorrowRecords(BorrowRecords borrowRecords) {
        this.borrowRecords = borrowRecords;
    }

    public Boolean getState() {
        return state;
    }

    public void setState(Boolean state) {
        this.state = state;
    }
}