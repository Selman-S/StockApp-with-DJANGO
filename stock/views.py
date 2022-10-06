
from rest_framework import viewsets,filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import (
    CategorySerializer,
    BrandSerializer,
    ProductSerializer,
    FirmSerializer,
    TransactionSerializer
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
  filter_backends = [filters.SearchFilter]
  search_fields = ['name']


class BrandView(viewsets.ModelViewSet):

  queryset = Brand.objects.all()
  serializer_class = BrandSerializer
  filter_backends = [filters.SearchFilter]
  search_fields = ['name']


class ProductView(viewsets.ModelViewSet):

  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  filter_backends = [DjangoFilterBackend,filters.SearchFilter]
  filterset_fields = ['category','brand']
  search_fields = ['name']


class FirmView(viewsets.ModelViewSet):
  queryset = Firm.objects.all()
  serializer = FirmSerializer
  search_fields = ['name']

class TransactionView(viewsets.ModelViewSet):
  queryset = Transaction.objects.all()
  serializer_class = TransactionSerializer