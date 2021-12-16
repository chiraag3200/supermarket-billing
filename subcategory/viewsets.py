from items.models import Item
from rest_framework import viewsets
from .serializers import SubCategorySerializer
from .models import SubCategory
from django.shortcuts import get_object_or_404


# to respond to subcategory API's
class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
  
    # to create a new subcategory
    def create(self, request):
        return super().create(request)

    # to update a subcategory
    def partial_update(self, request, pk=None):
        return super().partial_update(request)