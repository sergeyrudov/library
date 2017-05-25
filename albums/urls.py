from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Albums_display),
    url(r'^album/([0-9]+)', views.Album_view)
]



