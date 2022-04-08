from django.db import models


class StatusChoice(models.TextChoices):
    ORDER = 'order'
    ACCEPTED = 'accepted'
    FINISHED = 'finished'
