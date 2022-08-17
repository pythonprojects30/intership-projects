from django.db import models


# Create your models here.
class place(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='pic')
    description = models.TextField()

    def __str__(self):
        return self.name


class person(models.Model):
    name1 = models.CharField(max_length=300)
    img1 = models.ImageField(upload_to='pic')
    desc = models.TextField()

    def __str__(self):
        return self.name1
