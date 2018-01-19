from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=20, blank=True)
    lookingFor = models.CharField(max_length=20, blank=True)
    radius = models.IntegerField(blank=True, default=0)
    isNotification = models.BooleanField(default=False)
    isBeacon = models.BooleanField(default=False)
    subscriptionDate = models.CharField(max_length=50, blank=True)
    biography = models.CharField(max_length=10000, blank=True)
    profilePictureURL = models.CharField(max_length=200, blank=True)
    AuthenticationToken = models.CharField(max_length=150, blank=True)
    facebookToken = models.CharField(max_length=150, blank=True)
    DeviceType = models.CharField(max_length=100, blank=True)
    latitude = models.CharField(max_length=150, blank=True)
    longitude = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return str(self.id) + str(self.name)


class Favorites(models.Model):
    userID = models.IntegerField()
    otherUser = models.IntegerField()


class Block(models.Model):
    userID = models.IntegerField()
    otherUser = models.IntegerField()
