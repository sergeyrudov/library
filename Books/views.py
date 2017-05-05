from django.shortcuts import render
from .models import Author, Book
from django.http import HttpResponse

# Create your views here.


def book_request(request):
    di = Author.objects.all()
    authorname = []
    for i in di:
        authorname.append(i.name)
        for b in i.book_set.all():
            authorname.append(b.book_name)
    return HttpResponse('<br>'.join(authorname))


def book_author(request):
    allbooks = Book.objects.all()
    context = {'book': allbooks}
    return render(request, 'Books/allbooks.html', context)

#def find_by_author(request, get):
#    poisk =  Book.objects.all()
#    search = poisk[get].author.name
#    return HttpResponse(search)

def find_by_author(request, get):
    poisk = Author.objects.get(name=get)
    by_author = []
    for i in poisk.book_set.all():
         by_author.append(i.book_name)
    return HttpResponse('<br>'.join(by_author))


#!!!
def book_search_id(request,id):
    book = Book.objects.get(id=id)
    ac = book.comment_set.all()
    comments = []
    for i in ac:
        comments.append(book.book_name)
        comments.append(i.comment_text)
        comments.append(i.comments_link_user.name)
    return HttpResponse('<br>'.join((comments)))


def display_books_comments(request, id):
    author = Author.objects.get(id=id)
    author_name = []
    author_name.append(author.name)
    author_name.append(author.surname)
    bc = author.book_set.all()
    for i in bc:
        author_name.append(i.book_name)
        comments = i.comment_set.all()
        quantity = str(len(comments))
        author_name.append(quantity)
    return HttpResponse('<br>'.join(author_name))

def book_id(request, id):
    book = Book.objects.get(id=id)
    context = {'book': book}
    return render(request, 'Books/book.html', context)


def author_list(request):
    authorlist = Author.objects.all()
    allbooks = Book.objects.all()
    context = {'author': authorlist, 'allbooks': allbooks}
    return render(request, 'Books/allauthorsnbooks.html', context)

def author_id(request, id):
    authors_id = Author.objects.get(id=id)
    context = {'author_id': authors_id }
    return render(request, 'Books/authorbyid.html', context)

def book_info(request, id):
    book = Book.objects.get(id=id)
    context = {'books': book}
    return render(request,'Books/bookinfo.html', context)

def create_author(request):
    if request.GET:
        author = Author()
        author.name = request.GET['name']
        author.surname = request.GET['surname']
        author.save()
        return HttpResponse ('Все ок')
    return HttpResponse ('Вы не ввели данные')

def addbook(request, id):
    if request.GET:
        avtor = Author.objects.get(id=id)
        book = Book()
        book.book_name = request.GET['book_name']
        book.release_date = request.GET['release_date']
        book.author = avtor
        book.save()
    return HttpResponse('книга добавлена')






