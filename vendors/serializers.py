from rest_framework import serializers
from .models import Vendor


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = (
            'id',
            'user',
            'phone',
            'address',
            'store_name',
        )
        