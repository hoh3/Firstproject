from django.db import models
from django.contrib.auth.models import User

class Suggestion(models.Model):
    suggestion = models.CharField(max_length=140)

    def __str__(self):
        return self.suggestion

class Product(models.Model):
    name = models.CharField(max_length=140)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d',null=True, blank=True)
    price = models.IntegerField(default=0)
    description = models.TextField()

class Comment(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(User, null=True, blank=True)
    comments = models.ManyToManyField('Comment')

class Custom(models.Model):
    title = models.CharField(max_length=140)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(User, null=True, blank=True)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d', null=True, blank=True)

class Order(models.Model):
     author = models.ForeignKey(User, null=True, blank=True)
     product = models.ForeignKey(Product, null=True, blank=True)
     timestamp = models.DateTimeField(auto_now_add=True)

class Cart(models.Model):
     author = models.ForeignKey(User)
     order_time = models.DateField(null=True)
     payment_type = models.CharField(max_length=100, null=True)
