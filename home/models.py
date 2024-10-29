from django.db import models

# Create your models here.

class User(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=100)
    token=models.CharField(max_length=255)

    def __str__(self):
        return self.username

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    age = models.IntegerField(default=18)
    father_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class Book(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    