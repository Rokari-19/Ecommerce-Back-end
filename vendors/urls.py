from django.urls import path
from .views import *
urlpatterns = [
    path('create/', CreateVendorView.as_view()),
    path('list/', GetVendorListView.as_view()),
]