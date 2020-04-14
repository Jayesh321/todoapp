from django.db import models

# Create your models here.
class TOdoItem(models.Model):
    content = models.TextField()