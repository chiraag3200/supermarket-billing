from rest_framework import routers
from category.viewsets import *
from subcategory.viewsets import *
from items.viewsets import *
from category.viewsets import *

router = routers.DefaultRouter()


# route to items api's
router.register('items', ItemViewSet, basename='items')

# route to category api's
router.register('category', CategoryViewSet, basename='category')

# route to subcategory api's
router.register('subcategory', SubCategoryViewSet, basename='subcategory')

