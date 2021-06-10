from django.db import models


# Create your models here.
class Player(models.Model):
    playerName = models.TextField(unique=True)


class Character(models.Model):
    TYPE_CHOICES = (
        ('SPEED', "Speed"),
        ('POWER', "Power"),
        ('CONTROL', "Control"),
        ('SPIN', "Spin"),
        ('ALL-ROUND', "All-Round")
    )
    characterName = models.TextField(unique=True)
    characterType = models.TextField(choices=TYPE_CHOICES)
