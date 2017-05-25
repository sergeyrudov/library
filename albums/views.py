from django.shortcuts import render
from .models import Photo, Album
from django.http import HttpResponse


# Create your views here.


def Albums_display(request):
    alb = Album.objects.all()
    context = {'albums': alb }
    return render(request, 'albums/albums.html', context)


def Album_view(request, id):
    view = Album.objects.get(id=id)
    context = {'album': view}
    return render(request, 'albums/album.html', context)