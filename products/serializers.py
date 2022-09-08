from rest_framework import serializers
from .models import *
# from rest_flex_fields import FlexFieldsModelSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer() # overwriting the default category property of the serializer
    class Meta:
        model = Product
        fields = '__all__'
        depth = 1    
        # when dont want to use nested class for every property (not reccommended because reverse lookup field can't be implemented)
        # reverse lookup field is only possible when using source in serializer and related_name in relational field

'''
# To check what sets of fields and validators are created.
>>> from products.serializers import ProductSerializer
>>> serializer = ProductSerializer()
>>> print(repr(serializer))
'''