from django.db import models
from taggit.managers import TaggableManager
from datetime import datetime
from django.contrib.auth.models import User

class Note(models.Model):
    time = models.DateTimeField(default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    title = models.CharField(max_length=100)
    cover = models.URLField()
    description = models.TextField()
    body = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=False)

    tags = TaggableManager()

    def __str__(self):  # Admin stuff
        return self.title


class Reference(models.Model):
    url = models.URLField()
    note = models.ForeignKey(Note, on_delete=models.CASCADE, null=True, blank=True, related_name='references')

    def __str__(self):  # Admin stuff
        return f"{self.url}"