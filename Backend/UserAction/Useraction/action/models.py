from django.db import models
from django.contrib.auth.models import User 


class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.IntegerField(null=False)
    product_name = models.CharField(max_length=200 ,blank=False)
    product_price = models.DecimalField(max_digits=10 ,decimal_places=2)
    delivary_address = models.CharField(max_length=400 ,blank=False)
    purchase_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"Product: {self.product_name} -> BY: {self.user.username}"
    
class Review(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, related_name='reviews')
    review_data = models.TextField(blank=True)
    RATING_CHOICES = [
        (1, '1 - Poor'),
        (2, '2 - Fair'),
        (3, '3 - Good'),
        (4, '4 - Very Good'),
        (5, '5 - Excellent'),
        ]
    rating = models.IntegerChoices(choices=RATING_CHOICES)
    
    def __str__(self) -> str:
        return f"Review by: {self.purchase.user.username}"