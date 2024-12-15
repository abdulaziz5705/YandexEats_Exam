from django.db import models

from restaurants.models import MenuModel
from users.models import UserModel

class Courier(models.Model):

    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name="courier_profile")
    vehicle_type = models.CharField(max_length=50, choices=[('bike', 'Bike'), ('car', 'Car'), ('on foot', 'Foot')], default='bike')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Courier {self.user.username}"

class OrderFromUser(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted by Courier', 'Accepted by Courier'),
        ('Ready for Pickup', 'Ready for Pickup'),
        ('Picked Up', 'Picked Up'),
        ('Delivered', 'Delivered'),
        ('Completed', 'Completed'),
    ]
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='order_user')
    product = models.ForeignKey(MenuModel, on_delete=models.CASCADE, related_name='order_menu')
    create_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return self.product.name





