from django.http import Http404
from .serializers import ProductSerializer, KeyFeatureSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.db.models import Q
from .models import *


# class based view for the latedt products to display at the landing page
class LatestProducts(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

# product detail class-based view
class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404
        # updated logic for the product detail view to show the key features of a product
    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        feature = product.key_features.all()
        features_serializer = KeyFeatureSerializer(feature, many=True)
        serializer = ProductSerializer(product)
        # print(feature)
        return Response(serializer.data)
    

# class based view for the category detail
class CategoryDetail(APIView):      
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404
        
    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)  # serializing the objects in the database to json format
        return Response(serializer.data) # returning the data to the front end. this is how django passes data to the front end
    

@api_view(['POST'])
# takes in the query argument to filter through the database for items related to that product
def search(request):
    query = request.data.get('query', '')
# logic if the query returns true or false
    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    else:
        return Response({'products': []})
    
    

