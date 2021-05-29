from django.db import models

class imagedata(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=100, unique=True)
    caption = models.CharField(max_length=100)
    url = models.CharField(max_length=100)

