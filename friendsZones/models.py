from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    lookingFor = models.CharField(max_length=20)
    radius = models.IntegerField()
    isNotification = models.BooleanField(default=False)
    isBeacon = models.BooleanField(default=False)
    subscriptionDate = models.CharField(max_length=50)
    biography = models.CharField(max_length=10000)
    profilePictureURL = models.CharField(max_length=200)
    deviceToken = models.CharField(max_length=150)
    facebookToken = models.CharField(max_length=150)


class Favorites(models.Model):
    userID = models.ForeignKey(User)
    otherUser = models.IntegerField()


class Block(models.Model):
    userID = models.ForeignKey(User)
    otherUser = models.IntegerField()