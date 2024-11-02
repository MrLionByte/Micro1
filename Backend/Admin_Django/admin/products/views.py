from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework import viewsets,status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        prducts = Product.objects.all()
        serializer = ProductSerializer(prducts, many=True)
        print("PRODUCT",prducts)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = ProductSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save() 
        print("PRODUCT",serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        product = get_object_or_404(Product, id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk=None):
        product = get_object_or_404(Product, id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print("PRODUCT",serializer)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        product = get_object_or_404(Product, id=pk) 
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

