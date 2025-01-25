from django.urls import path

from order import views

urlpatterns = [
    path('checkout/', views.checkout),
    path('checkout-delivery/', views.checkout_delivery),
    path('my-orders/', views.OrdersList.as_view()),  
]