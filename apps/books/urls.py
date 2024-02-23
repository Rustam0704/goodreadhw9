from django.urls import path

from apps.books.views import BookListView, BookDetailView, AddReviewView, AddAuthorView,BookCreateView

app_name = "books"

urlpatterns = [
    path('', BookListView.as_view(), name="book-list"),
    path('<slug:slug>/', BookDetailView.as_view(), name="book-detail"),
    path('<int:pk>', AddReviewView.as_view(), name="add-review"),
    path('authadd/', AddAuthorView.as_view(), name="add-author"),
    path('addbook/', BookCreateView.as_view(), name="book-create"),
]
