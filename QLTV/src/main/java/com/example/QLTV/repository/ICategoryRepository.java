package com.example.QLTV.repository;

import com.example.QLTV.model.Category;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ICategoryRepository extends JpaRepository<Category, Integer> {
}

