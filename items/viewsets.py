from rest_framework import viewsets
from .serializers import ItemSerializer
from .models import Item
from category.models import Category
from subcategory.models import SubCategory


# fuction to find intersection of two lists
def intersection(list1, list2):
    return list(set(list1) & set(list2))


# function to append items to a list
def addItems(list):
    items = Item.objects.all()
    for item in items:
        list.append(item)
    return list


# viewset to respond to items API's
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    # to return results of item search
    def get_queryset(self):

        queryset = []
        category_items = []
        subcategory_items = []
        items = []

        # search queries entered by the user
        category = self.request.query_params.get("category", None)
        subcategory = self.request.query_params.get("subcategory", None)
        name = self.request.query_params.get("name", None)

        # find items with a given category
        if category is not None:
            category = category.lower()
            category = Category.objects.filter(category = category).first()
            if category is None:
                return []
            category_id = category.id
            subcategory_queryset = SubCategory.objects.filter(category = category_id)
            items_queryset = Item.objects.all()
            for item in items_queryset:
                if item.subcategory in subcategory_queryset:
                    category_items.append(item)
        else:
            addItems(category_items)
        
        # find items with a given subcategory
        if subcategory is not None:
            subcategory = subcategory.lower()
            subcategory = SubCategory.objects.filter(subcategory = subcategory).first()
            if subcategory is None:
                return []
            items_queryset = Item.objects.all()
            for item in items_queryset:
                if item.subcategory == subcategory:
                    subcategory_items.append(item)
        else:
            addItems(subcategory_items)

        # find items with a given name
        if name is not None:
            name = name.lower()
            items_queryset = Item.objects.all()
            for item in items_queryset:
                if item.name == name:
                    items.append(item)
        else:
            addItems(items)

        return intersection(intersection(category_items,subcategory_items),items)


    # to get all the items
    def retrieve(self, request, pk=None):
        queryset = Item.objects.all()
        return queryset

    # to create a new item
    def create(self, request):
        return super().create(request)

    # to update an item
    def partial_update(self, request, pk=None):
        return super().partial_update(request)