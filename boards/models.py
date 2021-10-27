from django.db import models
from core.models import AbstractTimeStamped


class Board(AbstractTimeStamped):

    title = models.CharField(max_length=80)
    content = models.TextField()
    writer = models.ForeignKey("users.User", models.CASCADE, related_name="boards", blank=True, null=True)



