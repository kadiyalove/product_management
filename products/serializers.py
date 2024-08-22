from rest_framework import serializers
from .models import Product, Category, Sale

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = '__all__'

class SaleSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = Sale
        fields = '__all__'


class ProductPopularitySerializer(ProductSerializer):
    popularity_score = serializers.FloatField(read_only=True)

    class Meta(ProductSerializer.Meta):
        fields = '__all__'