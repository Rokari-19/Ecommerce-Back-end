from django.shortcuts import render
import stripe
from django.conf import settings
from django.contrib.auth.models import User
from django.http import Http404


# restapi imports
from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

# my api/models imports
from .models import Order, OrderItem
from .serializers import PaymentSerializer, MyPaymentSerializer, DeliveryOrderSerializer


# Create your views here.
stripe.api_key = settings.STRIPE_SECRET_KEY
@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
    serializer = PaymentSerializer(data=request.data)

    if serializer.is_valid():
        paid_amount = sum(item.get('quantity') * item.get('product').price for item in serializer.validated_data['items'])

        try:
            charge = stripe.PaymentIntent.create(
                amount=int(paid_amount * 100),
                currency=request.data.get('currency'),
                # description='Charge from decena.com',
                # source=serializer.validated_data['stripe_token']
            )
            stripe_payment_id = charge['client_secret']
            serializer.save(user=request.user, paid_amount=paid_amount, stripe_payment_id=stripe_payment_id)

            return Response({
                    'clientSecret': charge['client_secret'],
                    'payment': serializer.data,},
                    status=status.HTTP_201_CREATED
                    )
        except stripe.error.StripeError as e:
            return Response({'error': str(e)}, status=400)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    




    
@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout_delivery(request):
    serializer = DeliveryOrderSerializer(data=request.data)
    
    if serializer.is_valid():
        
        paid_amount = sum(item.get('quantity') * item.get('product').price for item in serializer.validated_data['items'])
        serializer.save(user=request.user, paid_amount=paid_amount)
        
        return Response(serializer.data, status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrdersList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        orders = Order.objects.filter(user=request.user)
        serializer = PaymentSerializer(orders, many=True)
        return Response(serializer.data)
    