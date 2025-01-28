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
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'category',
            'get_absolute_url',
            'description',
            'price',
            'get_image',
            'get_thumbnail',
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
        
        
class CreateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'description',)
        
    def create(self, validated_data):
        category = Category.objects.create(
            name=validated_data['name'],
            description=validated_data['description']
        )
        return category