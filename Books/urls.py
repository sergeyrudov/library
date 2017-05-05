from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^all-authors/', views.book_request),
    url(r'^all-books', views.book_author),
    url(r'^find-by-author-([a-zA-Z0-9]+)', views.find_by_author),
    url(r'^book-id-([0-9]+)', views.book_search_id),
    url(r'^comments-book-([0-9]+)', views.display_books_comments),
    url(r'^find-id-([0-9]+)', views.book_id),
    url(r'^all', views.author_list),
    url(r'^author-id-([0-9]+)', views.author_id),
    url(r'^book-info-([0-9]+)', views.book_info),
]



