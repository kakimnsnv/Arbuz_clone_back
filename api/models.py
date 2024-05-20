from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=255)
    name = models.CharField(max_length=255)
    remark = models.CharField(max_length=255, null=True, blank=True)
    tags = models.JSONField(null=True, blank=True)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    imageUrl = models.TextField()
    minAmount = models.DecimalField(decimal_places=2, max_digits=5)
    amountType = models.CharField(max_length=255)
    isLiked = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField('CartItem')
    
    def __str__(self):
        return f"{self.user.username}'s Cart"
    
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    
class Collection(models.Model):
    name = models.CharField(max_length=255)
    products = models.ManyToManyField(Product)
    
    def __str__(self):
        return self.name