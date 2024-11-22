from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password



# User Profile Model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.get_full_name()}"


# Author Model
class Author(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


# Book Model
class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="books")
    name = models.CharField(max_length=200)
    shelf_row = models.IntegerField()
    shelf_col = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Book Detail Model
class BookDetail(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="details")
    description = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Details of {self.book.name}"


# Image Model
class Img(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="images")
    url = models.ImageField(upload_to="book_images/")  # Đổi CharField -> ImageField
    is_active = models.BooleanField(default=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Image for {self.book.name}"


# Borrow Record Model
class BorrowRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="borrow_records")
    book_detail = models.ForeignKey(BookDetail, on_delete=models.CASCADE, related_name="borrow_records")
    borrow_date = models.DateField()  
    return_due_date = models.DateField()  
    return_date = models.DateField(null=True, blank=True)  
    is_returned = models.BooleanField(default=False)  
  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Borrow Record of {self.user.get_full_name()} for {self.book_detail.book.name}"


# Penalty Model
class Penalty(models.Model):
    borrow_record = models.OneToOneField(BorrowRecord, on_delete=models.CASCADE, related_name="penalty")
    is_paid = models.BooleanField(default=False)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Penalty for {self.borrow_record.user.get_full_name()}"


# Admin 
class Login(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith("pbkdf2"):
            self.password = make_password(self.password)  # Mã hóa mật khẩu
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

