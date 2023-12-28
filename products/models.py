from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
import uuid

class Category(models.Model):
    name = models.CharField(max_length = 30)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='category_images')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name


class Products(models.Model):
    title = models.CharField(max_length = 30,blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    image = models.ImageField( upload_to='products_images', blank=True, null=True)
    description = models.TextField(max_length = 100, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places =2, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.title)


class Bag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
    

class BagItem(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name = 'items')
    bag = models.ForeignKey(Bag, on_delete=models.CASCADE, related_name = 'bagitems')
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.product.title
    
    @property
    def price(self):
        new_price = self.product.price * self.quantity
        return new_price

