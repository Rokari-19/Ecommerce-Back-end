from django.shortcuts import render
from rest_framework.generics import *
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import VendorSerializer
from .models import *
'''wildcard import'''

# Create your views here.

class CreateVendorView(GenericAPIView):
    serializer_class = VendorSerializer
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            vendor = serializer.data
            return Response({
                'vendor': vendor["id"]
            },
            status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class GetVendorListView(APIView):
    def get(self, request):
        approved_vendors = Vendor.objects.filter(approved=True)
        serializer = VendorSerializer(approved_vendors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)