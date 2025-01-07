from django.http import Http404
from .serializers import ProductSerializer, KeyFeatureSerializer, CategorySerializer, CreateCategorySerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import *
from rest_framework.decorators import api_view
from django.db.models import Q
from .models import *
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


# class based view for the latedt products to display at the landing page
class LatestProducts(APIView):
    def get(self, request):
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    
class GetCategoriesView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

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
        return Response(serializer.data, status.HTTP_200_OK)
    
    
class CreateProductView(GenericAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer =  self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            product = serializer.data
            return Response({
                'product': product["id"]
                }, 
                status.HTTP_201_CREATED
                )
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

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
        return Response(serializer.data, status.HTTP_200_OK) # returning the data to the front end. this is how django passes data to the front end
    
class CreateCategoryView(GenericAPIView):
    serializer_class = CreateCategorySerializer
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            category = serializer.data
            return Response({
                'category': category
            }, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
# takes in the query argument to filter through the database for items related to that product
def search(request):
    query = request.data.get('query', '')
# logic if the query returns true or false
    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    
    else:
        return Response({'products': []})
    
    
'''
todo: 
notifications for creating products and categories
'''
