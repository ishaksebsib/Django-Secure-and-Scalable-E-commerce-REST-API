from decimal import Decimal
from rest_framework import serializers
from .models import Product, Collection


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title',  'unit_price',  'collection']

    collection = serializers.HyperlinkedRelatedField(
        queryset=Collection.objects.all(),
        view_name='collection-detail',
    )

    def caculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)
