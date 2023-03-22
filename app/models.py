from django.db import models

# Create your models here.

class school(models.Model):
    email=models.CharField(max_length=150)
    name=models.CharField(max_length=150)
    city=models.CharField(max_length=150)
    pincode=models.IntegerField()
    password=models.CharField(max_length=150)

    def __str__(self):
        return self.name


class students(models.Model):
    school_name=models.ForeignKey(school, on_delete=models.CASCADE)
    name=models.CharField(max_length=150)
    grade=models.CharField(max_length=150)
    username=models.CharField(max_length=150)
    password=models.CharField(max_length=150)