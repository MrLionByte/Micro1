# models.py
from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    image = models.URLField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0) 
    likes = models.PositiveIntegerField(default=0)

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    user_id = models.IntegerField()
    rating = models.PositiveSmallIntegerField()
    review_text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)