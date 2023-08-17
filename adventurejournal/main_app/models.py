from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


class CampaignPhoto(models.Model):
    url = models.CharField(max_length=200)
    campaign = models.ForeignKey

    def __str__(self):
        return f"Photo for campaign_id: {self.campaign_id} @{self.url}"
    

class ProfilePhoto(models.Model):
    url = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for user {self.user_username} @{self.url}"


class System(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name} System"


class Monster(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name} Creature"


class Item(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name} Item"


class PlayerCharacter(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name} character in {self.campaign_name}"


class NPC(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name} NPC in {self.campaign_name}"


class Encounter(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name} encounter in {self.campaign_name}"


class Note(models.Model):
    name = models.CharField(max_length=30)
    content = models.RichTextField()

    def __str__(self):
        return f"{self.name} note in {self.campaign_name}"


class NoteCategory(models.Model):
    name = models.CharField(max_length=30)
    notes = models.ForeignKey(Note, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.name} category in {self.campaign_name}"



class Campaign(models.Model):
    name = models.CharField(max_length=30)
    system = models.ForeignKey(System, on_delete=models.CASCADE, null=True)
    next_game = models.DateTimeField('Next Game', null=True)
    pcs = models.ForeignKey(PlayerCharacter, on_delete=models.CASCADE, null=True)
    gm = models.ForeignKey(User, on_delete=models.CASCADE)
    players = models.ManyToManyField(User, null=True)
    cover = models.ForeignKey(CampaignPhoto, on_delete=models.CASCADE, null=True)
    npcs = models.ManyToManyField(NPC, null=True)
    encounters = models.ForeignKey(Encounter, on_delete=models.CASCADE, null=True)
    categories = models.ForeignKey(NoteCategory, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse("campaign_detail", kwargs={"campaign_id": self.id})
    