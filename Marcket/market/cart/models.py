from django.db import models
from django.contrib.auth.models import User
import home.models as mo
class CartItem(models.Model):
    item = models.ForeignKey(mo.Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total=models.FloatField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'