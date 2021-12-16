from django.db import models
from djangodeletes.softdeletes import SoftDeletable, SoftDeleteQuerySet, SoftDeleteManager
from subcategory import models as subcategory_models


# Create your models here.
class Item(SoftDeletable, models.Model):
    name = models.CharField(max_length=50, blank = False)
    price = models.IntegerField()
    subcategory = models.ForeignKey(subcategory_models.SubCategory, on_delete=models.CASCADE)

    objects = SoftDeleteManager.from_queryset(SoftDeleteQuerySet)()

    def __str__(self):
        return self.name

