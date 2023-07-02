from rest_framework import serializers
from .models import *
from drf_writable_nested import WritableNestedModelSerializer
# from rest_flex_fields import FlexFieldsModelSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


# class ProductImageListSerializer(serializers.ListSerializer):
    # print('hi there')
    # def update(self, instance, validated_data):
        # print('h')
        # print(instance)
        # print(validated_data)

class ProductImageSerializer(serializers.ModelSerializer):
    # print('hi')
    class Meta:
        model = ProductImage
        fields = '__all__'
        # list_serializer_class = ProductImageListSerializer

class QuantityVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuantityVariant
        fields = '__all__'

class SizeVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizeVariant
        fields = '__all__'

class ColorVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorVariant
        fields = '__all__'

class ProductSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    category = CategorySerializer(required=False) # overwriting the default category property of the serializer
    images = ProductImageSerializer(many=True, read_only=True)
    quantity_type = QuantityVariantSerializer(required=False, allow_null=True)
    color_type = ColorVariantSerializer(required=False, allow_null=True)
    size_type = SizeVariantSerializer(required=False, allow_null=True)
    # image = serializers.CharField(max_length=200, min_length=None, allow_blank=True)
    upload_images = serializers.ListField(
        child = serializers.ImageField(max_length=10000, allow_empty_file=True),
        write_only=True
    )
    class Meta:
        model = Product
        fields = '__all__'
        depth = 2
        # when dont want to use nested class for every property (not reccommended because reverse lookup field can't be implemented)
        # reverse lookup field is only possible when using source in serializer and related_name in relational field

    def create(self, instance, validated_data):
        pass

    def update(self, instance, validated_data):
        # print(validated_data)
        upload_images = validated_data.pop('upload_images')
        category = validated_data.get('category')
        category_name = category['category_name']
        try:
            category = Category.objects.get(category_name=category_name)
        except:
            category = Category.objects.create(category_name=category_name)
        
        instance.category = category
        instance.save()
        # product = Product.objects.create(**validated_data)
        for image in upload_images:
            ProductImage.objects.create(product=instance, image=image)
        
        return instance


'''
# To check what sets of fields and validators are created.
>>> from products.serializers import ProductSerializer
>>> serializer = ProductSerializer()
>>> print(repr(serializer))
'''