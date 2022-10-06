from django.shortcuts import render
from rest_framework import viewsets

from .serializers import (
    CategorySerializer
)

# Create your views here.
from .models import (
  Category, 
  Brand,
  Product,
  Firm,
  Transaction,
)


class CategoryView(viewsets.ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer