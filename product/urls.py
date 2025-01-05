from django.urls import path, include
from .views import LatestProducts, ProductDetail, CreateProductView, CategoryDetail, CreateCategoryView, search
# url patterns in the server for latest products, search, product detail, and category detail
urlpatterns = [
    path('latest-products/', LatestProducts.as_view()),
    path('products/search/', search),
    path('product/create/', CreateProductView.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/',  ProductDetail.as_view()),
    path('products/<slug:category_slug>/', CategoryDetail.as_view()),
    path('category/create/', CreateCategoryView.as_view()),

]