from rest_framework import serializers
from .models import Category

# serializer to process the category data
class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('id', 'category')

