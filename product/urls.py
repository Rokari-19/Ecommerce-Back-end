from django.urls import path, include
from .views import LatestProducts, ProductDetail, CategoryDetail, search
# url patterns in the server for latest products, search, product detail, and category detail
urlpatterns = [
    path('latest-products/', LatestProducts.as_view()),
    path('products/search/', search),
    path('products/<slug:category_slug>/<slug:product_slug>/',  ProductDetail.as_view()),
    path('products/<slug:category_slug>/', CategoryDetail.as_view()),

]