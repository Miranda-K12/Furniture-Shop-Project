from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "კატეგორია"
        verbose_name_plural = "კატეგორიები"

class ProductImage(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='extra_images')
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.product.name}"
    
    class Meta:
        verbose_name = "პროდუქტის სურათი"
        verbose_name_plural = "პროდუქტის სურათები"
    

class Product(models.Model):
    COLOR_CHOICES = [
        ('White', 'White'),
        ('Black', 'Black'),
        ('Brown', 'Brown'),
        ('Grey', 'Grey'),
        ('Beige', 'Beige'),
    ]

    MATERIAL_CHOICES = [
        ('Wood', 'Wood'),
        ('Metal', 'Metal'),
        ('Glass', 'Glass'),
        ('Leather', 'Leather'),
        ('Fabric', 'Fabric'),
        ('Plastic', 'Plastic'),
    ]

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="კატეგორია")
    description = models.TextField(blank=True, verbose_name="აღწერა")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="ფასი")
    stock = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, default='White')
    material = models.CharField(max_length=20, choices=MATERIAL_CHOICES, default='Wood')
    main_image = models.ImageField(upload_to='products/')  # აუცილებელი სურათი
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "პროდუქტი"
        verbose_name_plural = "პროდუქტები"