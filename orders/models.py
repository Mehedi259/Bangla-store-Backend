from django.db import models

class Order(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    customer_name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    status = models.CharField(max_length=50, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)
    customer_img = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Order {self.id}"
