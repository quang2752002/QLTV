package com.example.QLTV.repository;

import com.example.QLTV.model.Book;
import org.springframework.data.jpa.repository.JpaRepository;

public interface IBookRepository extends JpaRepository<Book, Integer> {

}
