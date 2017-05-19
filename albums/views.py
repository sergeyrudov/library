from django.shortcuts import render
from .models import Photo, Album
from django.http import HttpResponse


# Create your views here.


def Albums_display(request):
    alb = Album.objects.all()
    context = {'albums': alb }
    return render(request, 'albums/albums.html', context)
