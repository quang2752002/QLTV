from django.contrib import admin
from .models import *

# UserProfile Admin
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'is_active', 'created_at', 'updated_at')  
    search_fields = ('user__username', 'user__email')  
    list_filter = ('is_active',)  


# Author Admin
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'is_active', 'created_at', 'updated_at')  
    search_fields = ('name',)  
    list_filter = ('is_active',)


# Category Admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'description', 'is_active', 'created_at', 'updated_at')  
    search_fields = ('name', 'description')  
    list_filter = ('is_active',)


# Book Admin
class BookAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'author', 'category', 'shelf_row', 'shelf_col', 'is_active', 'created_at', 'updated_at')  
    search_fields = ('name', 'author__name', 'category__name')  
    list_filter = ('is_active', 'author', 'category')


# BookDetail Admin
class BookDetailAdmin(admin.ModelAdmin):
    list_display = ('id','book', 'description', 'is_active', 'created_at', 'updated_at')  
    search_fields = ('book__name', 'description')  
    list_filter = ('is_active',)


# Img Admin
class ImgAdmin(admin.ModelAdmin):
    list_display = ('id','book', 'url', 'is_active', 'created_at', 'updated_at')  
    search_fields = ('book__name',)  
    list_filter = ('is_active',)


# BorrowRecord Admin
class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'book_detail', 'borrow_date', 'return_due_date', 'return_date', 'is_returned', 'created_at', 'updated_at')  
    search_fields = ('user__username', 'book_detail__book__name')  
    list_filter = ('is_returned', 'borrow_date', 'return_due_date')  


# Penalty Admin
class PenaltyAdmin(admin.ModelAdmin):
    list_display = ('id','borrow_record', 'is_paid', 'created_at', 'updated_at')  
    search_fields = ('borrow_record__user__username',)  
    list_filter = ('is_paid',)


# AdminUser Admin
class LoginAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email', 'is_staff', 'is_active', 'created_at', 'updated_at')  
    search_fields = ('name', 'email')  
    list_filter = ('is_staff', 'is_active')







admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookDetail, BookDetailAdmin)
admin.site.register(Img, ImgAdmin)
admin.site.register(BorrowRecord, BorrowRecordAdmin)
admin.site.register(Penalty, PenaltyAdmin)
admin.site.register(Login, LoginAdmin)

