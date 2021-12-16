from django.db.models import fields
import category
from rest_framework import serializers
from .models import Item

# serializer to process the items data
class ItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Item
        fields = ('id', 'name', 'price', 'subcategory')