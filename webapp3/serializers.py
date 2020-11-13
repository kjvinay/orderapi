from rest_framework import serializers
from datetime import datetime

from .models import company,product,order

class companySerializer(serializers.ModelSerializer):
    class Meta:
        model = company
        fields = ('name', 'gst')
class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = ( 'productname', 'companies','cost')

class orderSerializer(serializers.ModelSerializer):
      class Meta:
        model = order
        fields = ('purchased_ON','order_no','companies', 'productname','quantity','cost','totalprice','purchase_details')
        read_only_fields = ('order_no',)
        
      def create(self, validated_data):
            return order.objects.create(**validated_data)