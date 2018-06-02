from django.db import models


# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=50)
    singer = models.CharField(max_length=40)
    year = models.CharField(max_length=4)
    Nos = models.IntegerField()
    album_logo = models.CharField(max_length=300)

    def _str_(self):
        return self.title + ' === ' + self.singer


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=40)
    song_title = models.CharField(max_length=300)
    is_fav=models.BooleanField(default=False)
