from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from .models import Products
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def getProducts(request):
    products = Products.objects.all()
    product_serizalized = ProductSerializer(products, many=True)
    print(product_serizalized)
    return Response(product_serizalized.data)