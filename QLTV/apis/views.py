from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import *
from math import ceil
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.contrib.auth.models import User
from .serializer import UserSerializer



#category
@swagger_auto_schema(
    method='get',
    manual_parameters=[
        openapi.Parameter('name', openapi.IN_QUERY, description="Lọc theo tên danh mục", type=openapi.TYPE_STRING),
        openapi.Parameter('page', openapi.IN_QUERY, description="Số trang để phân trang", type=openapi.TYPE_INTEGER),
        openapi.Parameter('page_size', openapi.IN_QUERY, description="Số lượng mục trên mỗi trang", type=openapi.TYPE_INTEGER),
    ]
)
@api_view(['GET'])
def list_categories(request):
    name = request.query_params.get('name', None)
    page = int(request.query_params.get('page', 1))
    page_size = int(request.query_params.get('page_size', 2))

    categories = Category.objects.all()
    if name:
        categories = categories.filter(name__icontains=name)
    
    total_count = categories.count()
    total_pages = ceil(total_count / page_size)
    
    start = (page - 1) * page_size
    end = start + page_size
    paginated_categories = categories[start:end]

    serializer = CategorySerializer(paginated_categories, many=True)
    data = {
        "message": "Danh sách các danh mục",
        "status": "success",
        "categories": serializer.data,
        "total": total_count,
        "current_page": page,
        "total_pages": total_pages,
    }
    return Response(data)

# Lấy chi tiết danh mục theo ID
@swagger_auto_schema(
    method='get',
    responses={
        200: CategorySerializer,
        404: 'Category not found'
    }
)
@api_view(['GET'])
def get_category_by_id(request, pk):
    try:
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category)
        data = {
            "message": "Category details",
            "status": "success",
            "category": serializer.data,
        }
        return Response(data, status=status.HTTP_200_OK)
    except Category.DoesNotExist:
        return Response(
            {"message": "Category not found", "status": "error"},
            status=status.HTTP_404_NOT_FOUND
        )

# Tạo mới một danh mục
@swagger_auto_schema(
    method='post',
    request_body=CategorySerializer,
    responses={
        201: CategorySerializer,
        400: 'Bad Request'
    }
)
@api_view(['POST'])
def create_category(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Category created successfully", "status": "success", "category": serializer.data}, status=status.HTTP_201_CREATED)
    return Response({"message": "Failed to create category", "status": "error", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# Cập nhật danh mục theo ID
@swagger_auto_schema(
    method='put',
    request_body=CategorySerializer,
    responses={
        200: CategorySerializer,
        404: 'Category not found',
        400: 'Bad Request'
    }
)
@api_view(['PUT'])
def update_category(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({"message": "Category not found", "status": "error"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = CategorySerializer(category, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Category updated successfully", "status": "success", "category": serializer.data}, status=status.HTTP_200_OK)
    return Response({"message": "Failed to update category", "status": "error", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# Xóa danh mục theo ID
@swagger_auto_schema(
    method='delete',
    responses={
        204: 'Category deleted successfully',
        404: 'Category not found'
    }
)
@api_view(['DELETE'])
def delete_category(request, pk):
    try:
        category = Category.objects.get(pk=pk)
        category.delete()
        return Response({"message": "Category deleted successfully", "status": "success"}, status=status.HTTP_204_NO_CONTENT)
    except Category.DoesNotExist:
        return Response({"message": "Category not found", "status": "error"}, status=status.HTTP_404_NOT_FOUND)
    



# book
@swagger_auto_schema(
    method='get',
    manual_parameters=[
        openapi.Parameter('categoryId', openapi.IN_QUERY, description="Lọc theo danh mục", type=openapi.TYPE_INTEGER),
        openapi.Parameter('page', openapi.IN_QUERY, description="Số trang để phân trang", type=openapi.TYPE_INTEGER),
        openapi.Parameter('page_size', openapi.IN_QUERY, description="Số lượng mục trên mỗi trang", type=openapi.TYPE_INTEGER),
    ]
)
@api_view(['GET'])
def list_books(request):
    # Lấy tham số từ query string
    categoryId = request.query_params.get('categoryId', None)
    page = int(request.query_params.get('page', 1))
    page_size = int(request.query_params.get('page_size', 2))

    # Lấy tất cả các sách
    books = Book.objects.all()

    if categoryId:
        books = books.filter(category_id=categoryId)  

    # Đếm tổng số sách
    total_count = books.count()

    # Tính tổng số trang
    total_pages = ceil(total_count / page_size)

    # Phân trang thủ công
    start = (page - 1) * page_size
    end = start + page_size
    paginated_books = books[start:end]

    # Serialize dữ liệu sách
    serializer = BookSerializer(paginated_books, many=True)

    # Chuẩn bị dữ liệu trả về
    data = {
        "message": "Danh sách ",
        "status": "success",
        "books": serializer.data,
        "total": total_count,
        "current_page": page,
        "total_pages": total_pages,
    }

    return Response(data)

@swagger_auto_schema(
    method='post',
    request_body=BookSerializer,
    responses={
        201: BookSerializer,
        400: 'Bad Request'
    }
)
@api_view(['POST'])
def create_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Book created successfully", "status": "success", "category": serializer.data}, status=status.HTTP_201_CREATED)
    return Response({"message": "Failed to create Book", "status": "error", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='get',
    responses={
        200: BookSerializer,
        404: 'Book not found'
    }
)
@api_view(['GET'])
def get_book_by_id(request, pk):

    try:
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book)
        data = {
            "message": "Book ",
            "status": "success",
            "book": serializer.data,
        }
        return Response(data, status=status.HTTP_200_OK)
    except Category.DoesNotExist:
        return Response(
            {"message": "Category not found", "status": "error"},
            status=status.HTTP_404_NOT_FOUND
        )

@swagger_auto_schema(
    method='put',
    request_body=BookSerializer,
    responses={
        200: BookSerializer,
        404: 'Book not found',
        400: 'Bad Request'
    }
)
@api_view(['PUT'])
def update_book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response({"message": "Book not found", "status": "error"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = BookSerializer(book, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Book updated successfully", "status": "success", "Book": serializer.data}, status=status.HTTP_200_OK)
    return Response({"message": "Failed to update book", "status": "error", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


#bookdetail
@swagger_auto_schema(
    method='get',
    manual_parameters=[
        openapi.Parameter('bookId', openapi.IN_QUERY, description="Lọc theo BookId", type=openapi.TYPE_INTEGER),
        openapi.Parameter('page', openapi.IN_QUERY, description="Số trang để phân trang", type=openapi.TYPE_INTEGER),
        openapi.Parameter('page_size', openapi.IN_QUERY, description="Số lượng mục trên mỗi trang", type=openapi.TYPE_INTEGER),
    ]
)
@api_view(['GET'])
def list_bookdetail(request):
    bookId = request.query_params.get('bookId', None)
    page = int(request.query_params.get('page', 1))
    page_size = int(request.query_params.get('page_size', 2))
    
    book_detail = BookDetail.objects.all()
    if bookId:
        book_detail = book_detail.filter(book_id=bookId)
    
    total_count = book_detail.count()
    total_pages = ceil(total_count / page_size)
    
    start = (page - 1) * page_size
    end = start + page_size
    paginated_categories = book_detail[start:end]

    serializer = BookDetailSerializer(paginated_categories, many=True)
    data = {
        "message": "Danh sách sách chi tiết",
        "status": "success",
        "categories": serializer.data,
        "total": total_count,
        "current_page": page,
        "total_pages": total_pages,
    }
    return Response(data)


