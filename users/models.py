from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20)
    address = models.TextField()
    birth_date = models.DateField(null=True, blank=True)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "მომხმარებელი"
        verbose_name_plural = "მომხმარებლები"