from rest_framework import viewsets, filters
from .models import Product, Category, Sale
from .serializers import ProductSerializer, CategorySerializer, SaleSerializer, ProductPopularitySerializer
from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import F, Sum, ExpressionWrapper, FloatField, Case, When


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description', 'category__name']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

    # Custom action to calculate product popularity
    @action(detail=False, methods=['get'])
    def product_popularity(self, request):

        products = Product.objects.annotate(
                total_sales=Sum('sales__quantity'),
                total_products=F('inventory_count')
            ).annotate(
                popularity_score=ExpressionWrapper(
                    Case(
                        When(total_products__gt=0, then=F('total_sales') * 100.0 / F('total_products')),
                        default=0,
                        output_field=FloatField()
                    ),
                    output_field=FloatField()
                )
            ).order_by('-popularity_score')

        serializer = ProductPopularitySerializer(products, many=True)

        return Response(serializer.data)
