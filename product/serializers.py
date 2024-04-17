from rest_framework import serializers
from .models import *
# import statements

# a serializer allows python data to be converted to json form

class KeyFeatureSerializer(serializers.ModelSerializer):
    # creating the KeyFeatures serializer to serialize the key features model
    class Meta:
        model = KeyFeature
        fields = ('id', 'name',) 
class ProductSerializer(serializers.ModelSerializer):
    key_features = KeyFeatureSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'get_absolute_url',
            'description',
            'price',
            'get_image',
            'get_thumbnail',
            'key_features'
        )


# creating the serializer for the category view. like in the product serializer,
# i initialized the ProductSerializer to pass in the necessary data partaining to the product
class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = Category
        fields = (
            'id', 
            'name',
            'get_absolute_url',
            'products',
            'description',
        )