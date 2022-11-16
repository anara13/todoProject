from audioop import reverse
from django.db import models

# Create your models here.

class ToDo(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse("todo", args=[self.id])