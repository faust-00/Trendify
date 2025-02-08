from django.db import models
from django.db.models import DateTimeField, CASCADE

from user.models import User
from product.models import Product

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.CharField(max_length=15, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('canceled', 'Canceled')])
    created_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pk}: {self.user}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    created_at = models.DateTimeField(auto_now_add=True)


class Card(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pk}: {self.user}"


class CardItem(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=CASCADE, related_name='card_items')
    created_at = models.DateTimeField(auto_now_add=True)

