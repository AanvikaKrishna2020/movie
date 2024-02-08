from django.db import models

# Create your models here.
class Movie(models.Model):
    code=models.CharField(max_length=250)
    name=models.TextField()
    price=models.IntegerField()
    img=models.ImageField(upload_to='gallery')

    def __str__(self):
       return self.code