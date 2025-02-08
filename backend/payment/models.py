from django.db import models
from order.models import Order

class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('paid', 'Paid'), ('failed', 'Failed')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order