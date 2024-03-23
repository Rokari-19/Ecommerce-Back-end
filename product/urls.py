from django.urls import path, include
from .views import LatestProducts, ProductDetail

urlpatterns = [
    path('latest-products/', LatestProducts.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/',  ProductDetail.as_view()),
    
]