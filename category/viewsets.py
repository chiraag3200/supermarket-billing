from items.models import Item
from rest_framework import viewsets
from .serializers import CategorySerializer
from .models import Category


# viewset to respond to category API's
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # to create a new category
    def create(self, request):
        return super().create(request)

    # to update a category
    def partial_update(self, request, pk=None):
        return super().partial_update(request)