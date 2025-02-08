from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=256)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='category_products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title