from django.db import models

# Create your models here.

class Album(models.Model):
    title = models.CharField('Name the albumx', max_length=250)
    descr = models.TextField('Full description', blank=True)
    date_created = models.DateTimeField('Date created',auto_now_add = True, auto_created = True)
    date_change = models.DateTimeField('Date change', auto_now_add= True, auto_created=True)

    def __str__(self):
        return '{0} - {1}'.format(self.title, self.descr)


class Photo(models.Model):
    alt = models.TextField()
    img = models.ImageField(upload_to='albums/static/albums/photos')
    date_created = models.DateTimeField('Date created', auto_now_add=True, auto_created=True)
    date_change = models.DateTimeField('Date change', auto_now_add=True, auto_created=True)
    album = models.ForeignKey(Album)

    def static_url(self):
        return self.url.split('/', 2)[2]

    def __str__(self):
        return self.alt

