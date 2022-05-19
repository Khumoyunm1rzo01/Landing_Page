from distutils.command import upload
from turtle import mode
from xml.parsers.expat import model
from django.db import models

# Create your models here.

class Title(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    rasm = models.ImageField(upload_to='title/')


    def __str__(self):
        return self.title
class Project(models.Model):
    project = models.CharField(max_length=255)

    def __str__(self):
        return self.project

class Team(models.Model):
    team = models.CharField(max_length=255)

    def __str__(self):
        return self.team
class About(models.Model):
    about = models.CharField(max_length=255)

    def __str__(self):
        return self.about
class Me(models.Model):
    me = models.CharField(max_length=255)

    def __str__(self):
        return self.me

class Design(models.Model):
    design = models.CharField(max_length=255)

    def __str__(self):
        return self.design

class YoutubeVideo(models.Model):
    video = models.CharField(max_length=255)

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.IntegerField()
    subject = models.CharField(max_length=355)
    message = models.TextField()

class Telegram_ids(models.Model):
    ids = models.IntegerField()
    