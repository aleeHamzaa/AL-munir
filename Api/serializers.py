from datetime import timezone
from django.db import models
from django.utils.translation import check_for_language
from rest_framework import fields, serializers
from .models import Product
from .models import Product_1

class Productserializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id','Name','Number','Warhouse']
class Product1serializer(serializers.ModelSerializer):
    class Meta:
        model=Product_1
        fields=['id','Name','Qty','Warhouse','serial_num','color','model_type','capisty']
