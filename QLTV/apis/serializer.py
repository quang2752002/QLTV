from rest_framework import serializers
from .models import Author, Category, Book, BookDetail, Img, BorrowRecord, Penalty, Login
from django.contrib.auth.models import User


# Serializer for User
class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        exclude = ['password', 'username', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'user_permissions']
    
    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}".strip()


# Serializer for Author
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'is_active', 'created_at', 'updated_at']


# Serializer for Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'is_active', 'created_at', 'updated_at']


# Serializer for Book
class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.name')
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Book
        fields = [
            'id', 'author', 'author_name', 'category', 'category_name',
            'name', 'shelf_row', 'shelf_col', 'description', 'is_active', 
            'created_at', 'updated_at'
        ]


# Serializer for BookDetail
class BookDetailSerializer(serializers.ModelSerializer):
    book_name = serializers.ReadOnlyField(source='book.name')

    class Meta:
        model = BookDetail
        fields = ['id', 'book', 'book_name', 'description', 'is_active', 'created_at', 'updated_at']


# Serializer for Img
class ImgSerializer(serializers.ModelSerializer):
    book_name = serializers.ReadOnlyField(source='book.name')

    class Meta:
        model = Img
        fields = ['id', 'book', 'book_name', 'url', 'is_active', 'created_at', 'updated_at']


# Serializer for BorrowRecord
class BorrowRecordSerializer(serializers.ModelSerializer):
    user_full_name = serializers.ReadOnlyField(source='user.get_full_name')
    book_name = serializers.ReadOnlyField(source='book_detail.book.name')

    class Meta:
        model = BorrowRecord
        fields = [
            'id', 'user', 'user_full_name', 'book_detail', 'book_name', 
            'borrow_date', 'return_due_date', 'return_date', 
            'is_returned', 'created_at', 'updated_at'
        ]


# Serializer for Penalty
class PenaltySerializer(serializers.ModelSerializer):
    user_full_name = serializers.ReadOnlyField(source='borrow_record.user.get_full_name')

    class Meta:
        model = Penalty
        fields = ['id', 'borrow_record', 'user_full_name', 'is_paid', 'created_at', 'updated_at']


# Serializer for Login
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ['id', 'name', 'email', 'password', 'is_staff', 'is_active', 'created_at', 'updated_at']
        extra_kwargs = {'password': {'write_only': True}}  # Mật khẩu chỉ được ghi, không được hiển thị
