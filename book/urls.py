from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_view, name='book'),
    path('book_detail/<int:id>/', views.book_view_detail, name='detail'),
    path('book/<int:id>/update/', views.update_book_view, name='update'),
    path('book/<int:id>/delete/', views.delete_book_view, name='delete'),
    path('add_book/', views.add_book_view, name='create_book'),
]