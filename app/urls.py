from django.urls import path
from .views import (
                        BookListView, 
                        BookDetailView,
                        BookCreateView,
                        BookUpdateView,
                        BookDeleteView,
                        AutherListView,
                        AutherDetailView,
                        AutherCreateView, 
                        AutherUpdateView, 
                        AutherDeleteView
                    )

urlpatterns = [
    path('book/', BookListView.as_view(), name='book_list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('create-book/', BookCreateView.as_view(), name='book_create'),
    path('update-book/<int:pk>', BookUpdateView.as_view(), name='book_update'),
    path('delete-book/<int:pk>', BookDeleteView.as_view(), name='book_delete'),

    path('auther/', AutherListView.as_view(), name='auther_list'),
    path('auther/<int:pk>/', AutherDetailView.as_view(), name='auther_detail'),
    path('create-auther/', AutherCreateView.as_view(), name='auther_create'),
    path('update-auther/<int:pk>', AutherUpdateView.as_view(), name='auther_update'),
    path('delete-auther/<int:pk>', AutherDeleteView.as_view(), name='auther_delete'),
]