from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField('Имя автора', max_length= 250)
    surname = models.CharField('Фамилия автора', max_length=250)

    def __str__(self):
        return self.name

class Book(models.Model):
    author = models.ForeignKey(Author)
    book_name = models.CharField('Название книги', max_length=250)
    release_date = models.DateField('Дата выпуска', )

    def __str__(self):
        return self.book_name

class Comment(models.Model):
    comments_link_user = models.ForeignKey('User')
    comments_link_author = models.ForeignKey(Author, blank= True,null=True)
    comments_link_book = models.ForeignKey(Book, blank=True, null=True)
    comment_text = models.TextField('текст комментария', max_length=250)

class User (models.Model):
    name = models.CharField('Имя автора', max_length=250)
    surname = models.CharField('фамилия автора', max_length=250)


