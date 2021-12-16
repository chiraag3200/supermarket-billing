from rest_framework import serializers
from .models import SubCategory


# to process the subcategory data
class SubCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SubCategory
        fields = ('__all__')