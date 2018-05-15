from django.db import models
from django.utils import timezone


class Item(models.Model):
    title = models.CharField(max_length=200)
    done = models.BooleanField()
    author_ip = models.CharField(max_length=20)
    # stores utc time
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
