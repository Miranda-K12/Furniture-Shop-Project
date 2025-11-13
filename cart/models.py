from django.db import models
from users.models import CustomUser
from products.models import Product
from django.db import models


class Cart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    def get_total_price(self):
        total = 0
        for item in self.cartitem_set.all():
            total += item.product.price * item.quantity
        return total

    def get_total_items(self):
        return self.cartitem_set.count()
    
    def get_total_items_count(self):
        return sum(item.quantity for item in self.cartitem_set.all())

    def __str__(self):
        return f"Cart of {self.user}"
    
    class Meta:
        verbose_name = "კალათა"
        verbose_name_plural = "კალათები"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
    
    class Meta:
        verbose_name = "კალათის ნივთი"
        verbose_name_plural = "კალათის ნივთები"
