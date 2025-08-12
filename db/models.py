from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class Skill(models.Model):
    name = models.CharField(max_length=255)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)


class Guild(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class Player(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    bio = models.TextField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    guild = models.ForeignKey(Guild, on_delete=models.SET_NULL)
    created_add = models.DateTimeField(auto_now_add=True)
