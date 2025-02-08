from django.db import models
from user.models import User
from product.models import Product

class Comment(models.Model):
    review_text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='products')
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.review_text[100:]


class Rating(models.Model):

    class Score(models.IntegerChoices):
        one = 1, "1"
        two = 2, "2"
        three = 3, "3"
        four = 4, "4"
        five = 5, "5"

    score = models.IntegerField(choices=Score.choices)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

