from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.list_categories, name='list_categories'),
    path('categories/create/', views.create_category, name='create_category'),
    path('categories/update/<int:pk>/', views.update_category, name='update_category'),
    path('categories/delete/<int:pk>/', views.delete_category, name='delete_category'),
    path('categories/<int:pk>/', views.get_category_by_id, name='get_category_by_id'),  
 
    path('books/', views.list_books, name='list_books'),
    path('books/create/', views.create_book, name='create_book'),
    path('books/update/<int:pk>/', views.update_book, name='update_category'),
    path('books/<int:pk>/', views.get_book_by_id, name='get_category_by_id'), 

    path('bookdetail/', views.list_bookdetail, name='list_bookdetail'),

]
