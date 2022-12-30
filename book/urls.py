from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.BookView.as_view(), name='book'),
    path('book_detail/<int:id>/', views.BookDetailView.as_view(), name='detail'),
    path('book/<int:id>/update/', views.BookUpdateView.as_view(), name='update'),
    path('book/<int:id>/delete/', views.BookDeleteView.as_view(), name='delete'),
    path('add_book/', views.BookCreateView.as_view(), name='create_book'),
]