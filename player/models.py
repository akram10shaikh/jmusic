from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Song(models.Model):
    id = models.AutoField(primary_key=True)
    song_name = models.CharField(max_length=100,null=True)
    song = models.FileField(upload_to='song/')
    song_image = models.FileField(upload_to='image/')
    category = models.CharField(max_length=100,choices=(('Old is Gold','Old is Gold'),('Latest Hit','Latest Hit'),('Hit of Salman','Hit of Salman'),('90s Hits','90s Hits')),null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.song_name

class Playlist(models.Model):
    song = models.ForeignKey(Song,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

