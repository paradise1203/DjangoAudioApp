# coding=utf-8
from django.contrib.auth.models import User
from django.db import models

genres = (
    ("rock", "Rock"),
    ("hm", "Heavy Metal"),
    ("pop", "Pop music"),
    ("pth", "Patriotic Trance House")
)


class Audio(models.Model):
    class Meta:
        db_table = "audios"
        verbose_name_plural = u'Аудиозаписи'
        unique_together = ['title', 'artist']

    title = models.CharField(max_length=50)
    artist = models.ForeignKey('Artist', related_name="audio_personal", null=True)
    album = models.CharField(max_length=50, blank=True)
    anon_likes = models.IntegerField(default=0)
    genre = models.CharField(max_length=4, choices=genres, null=True)
    favorite = models.ManyToManyField(User, related_name="favorites")

    def __unicode__(self):
        return "%s : %s : %s : %s : %s" % (self.artist, self.title, self.album, self.anon_likes, self.genre)


class Artist(models.Model):
    class Meta:
        db_table = "artists"

    name = models.CharField(max_length=50, unique=True)
    country = models.CharField(max_length=30, blank=True)

    def __unicode__(self):
        return self.name


class Duet(Audio):
    artist2 = models.ForeignKey('Artist', related_name='audios_from_duet', null=True)


