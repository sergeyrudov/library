from django.contrib import admin
from .models import Author, Book, Comment, User
# Register your models here.

class BookInline(admin.TabularInline):
    model = Book

class Author_admin(admin.ModelAdmin):
    inlines = [BookInline]


admin.site.register(Book)
admin.site.register(Author, Author_admin)
admin.site.register(Comment)
admin.site.register(User)



