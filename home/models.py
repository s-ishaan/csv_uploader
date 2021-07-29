from django.db import models

# Create your models here.
class Data(models.Model):
    title = models.FileField(max_length=100, upload_to='media')
