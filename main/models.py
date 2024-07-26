from django.db import models
from accaunts.models import CustomUser
# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=212)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
