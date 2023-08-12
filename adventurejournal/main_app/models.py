from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


class Campaign(models.Model):
    name = models.CharField(max_length=30)


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


class System(models.Model):
    name = models.CharField(max_length=20)