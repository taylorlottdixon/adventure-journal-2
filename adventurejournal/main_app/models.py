from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


class Photo(models.Model):
  url = models.CharField(max_length=200)


class System(models.Model):
    name = models.CharField(max_length=20)


class Monster(models.Model):
    name = models.CharField(max_length=20)


class Item(models.Model):
    name = models.CharField(max_length=30)


class PlayerCharacter(models.Model):
    name = models.CharField(max_length=20)


class NPC(models.Model):
    name = models.CharField(max_length=20)


class Encounter(models.Model):
    name = models.CharField(max_length=20)


class Campaign(models.Model):
    name = models.CharField(max_length=30)
    system = models.ForeignKey(System, on_delete=models.CASCADE, null=True)
    next_game = models.DateTimeField('Next Game', null=True)
    players = models.ManyToManyField(PlayerCharacter)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    cover = models.ForeignKey(Photo, on_delete=models.CASCADE, null=True)
    npcs = models.ManyToManyField(NPC)

    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse("campaign_detail", kwargs={"campaign_id": self.id})
    