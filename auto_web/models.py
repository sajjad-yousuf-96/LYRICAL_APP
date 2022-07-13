from django.db import models

# Create your models here.

class Lyrics(models.Model):
    song_name=models.CharField(max_length=300,null=True)
    song_lyrics=models.CharField(max_length=300,null=True)
    song_artist=models.CharField(max_length=300,null=True)
    time_stamp=models.CharField(max_length=300,null=True)

    def __str__(self):
        self.song_name