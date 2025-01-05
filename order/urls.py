from django.urls import path

from order import views

urlpatterns = [
    path('checkout/', views.checkout),
    path('my-orders/', views.OrdersList.as_view()),  
]