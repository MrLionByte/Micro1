from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Review, Purchase

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class PurchaseSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Purchase
        fields = ['id', 'user', 'product_id', 'product_name', 
                  'product_price', 'delivary_address', 'purchase_date']

class ReviewSerializer(serializers.ModelSerializer):
    purchase = serializers.PrimaryKeyRelatedField(queryset=Purchase.objects.all())  
    
    class Meta:
        model = Review
        fields = ['id','purchase','review_data', 'rating']
 