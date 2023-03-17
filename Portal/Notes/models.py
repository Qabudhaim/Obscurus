from django.db import models
from taggit.managers import TaggableManager
from datetime import datetime
class Note(models.Model):
    time = models.DateTimeField(default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    title = models.CharField(max_length=100)
    description = models.TextField()
    body = models.TextField()

    tags = TaggableManager()

    def __str__(self):  # Admin stuff
        return self.title


class Reference(models.Model):
    link = models.TextField()
    note = models.ForeignKey(Note, on_delete=models.CASCADE, null=True, blank=True, related_name='references')

    def __str__(self):  # Admin stuff
        return f"{self.link}"