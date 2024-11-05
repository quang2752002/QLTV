package com.example.QLTV.controller;

import com.example.QLTV.model.Category;
import com.example.QLTV.model.ResponseObject;
import com.example.QLTV.repository.ICategoryRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.http.HttpStatus;
import org.springframework.scheduling.annotation.Async;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.concurrent.CompletableFuture;

@RestController
@RequestMapping(path = "api/category")
public class CategoryController {

    private final ICategoryRepository categoryRepository;

    @Autowired
    public CategoryController(ICategoryRepository categoryRepository) {
        this.categoryRepository = categoryRepository;
    }
    @GetMapping("/getAll")
    @Async
    public CompletableFuture<ResponseEntity<ResponseObject>> getAllCategory() {
        return CompletableFuture.supplyAsync(() -> {
            List<Category> categories = categoryRepository.findAll();
            if (categories == null || categories.isEmpty()) {
                ResponseObject responseObject = new ResponseObject(HttpStatus.NOT_FOUND, "No categories found", null);
                return ResponseEntity.status(HttpStatus.NOT_FOUND).body(responseObject);
            }
            ResponseObject responseObject = new ResponseObject(HttpStatus.OK, "Categories retrieved successfully", categories);
            return ResponseEntity.ok(responseObject);
        });
    }

    @GetMapping("/getCategory/{id}")
    public ResponseEntity<ResponseObject> getCategoryById(@PathVariable int id) {
        Category category = categoryRepository.findById(id).orElse(null);
        if (category == null) {
            ResponseObject responseObject = new ResponseObject(HttpStatus.NOT_FOUND, "Category not found", null);
            return ResponseEntity.status(HttpStatus.NOT_FOUND).body(responseObject);
        }
        ResponseObject responseObject = new ResponseObject(HttpStatus.OK, "Category retrieved successfully", category);
        return ResponseEntity.ok(responseObject);
    }
    @PostMapping("/add")
    @Async
    public CompletableFuture<ResponseEntity<ResponseObject>> addCategory(@RequestBody Category category) {
        return CompletableFuture.supplyAsync(() -> {
            Category savedCategory = categoryRepository.save(category);
            ResponseObject responseObject = new ResponseObject(HttpStatus.CREATED, "Category added successfully", savedCategory);
            return ResponseEntity.status(HttpStatus.CREATED).body(responseObject);
        });
    }

    @PutMapping("/update/{id}")
    public ResponseEntity<ResponseObject> updateCategory(@PathVariable int id, @RequestBody Category updatedCategory) {
        return categoryRepository.findById(id)
                .map(existingCategory -> {
                    existingCategory.setName(updatedCategory.getName()); // Update other fields as necessary
                    Category savedCategory = categoryRepository.save(existingCategory);
                    ResponseObject responseObject = new ResponseObject(HttpStatus.OK, "Category updated successfully", savedCategory);
                    return ResponseEntity.ok(responseObject);
                })
                .orElseGet(() -> {
                    ResponseObject responseObject = new ResponseObject(HttpStatus.NOT_FOUND, "Category not found", null);
                    return ResponseEntity.status(HttpStatus.NOT_FOUND).body(responseObject);
                });
    }

    @DeleteMapping("/delete/{id}")
    public ResponseEntity<ResponseObject> deleteCategory(@PathVariable int id) {
        return categoryRepository.findById(id)
                .map(existingCategory -> {
                    categoryRepository.delete(existingCategory);
                    ResponseObject responseObject = new ResponseObject(HttpStatus.NO_CONTENT, "Category deleted successfully", null);
                    return ResponseEntity.status(HttpStatus.NO_CONTENT).body(responseObject);
                })
                .orElseGet(() -> {
                    ResponseObject responseObject = new ResponseObject(HttpStatus.NOT_FOUND, "Category not found", null);
                    return ResponseEntity.status(HttpStatus.NOT_FOUND).body(responseObject);
                });
    }
}
