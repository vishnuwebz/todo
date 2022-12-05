from django.db import models

# Create your models here.
class Programmers(models.Model):
    pname = models.CharField(max_length=250)
    pimg=models.ImageField(upload_to='image1')
    ptext=models.TextField()

    def __str__(self):
        return self.pname

class Languages(models.Model):
    lname=models.CharField(max_length=250)
    limg=models.ImageField(upload_to='image2')
    ltext=models.TextField()

    def __str__(self):
        return self.lname

class Languagesbg(models.Model):
    lbimg=models.ImageField(upload_to='image3')

    def __str__(self):
        return self.lbimg
