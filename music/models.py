from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
class Album(models.Model):
    user = models.ForeignKey(User,default=1)
    artist = models.CharField(max_length=100)
    album_title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()
    def get_absolute_url(self):
        return reverse('music/detail.html', kwargs={'pk':self.pk })
    def __str__(self):
        return self.album_title + '-' + self.artist

class Song(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    audio_file = models.FileField(default='')
    song_title = models.CharField(max_length=200)
    def __str__(self):
        return self.song_title

