from django.db import models
from djangodeletes.softdeletes import SoftDeletable, SoftDeleteQuerySet, SoftDeleteManager
from category import models as category_models


# Create your models here.
class SubCategory(SoftDeletable, models.Model):
    subcategory = models.CharField(max_length=50, null=False, blank = False)
    category = models.ForeignKey(category_models.Category, on_delete=models.CASCADE)

    objects = SoftDeleteManager.from_queryset(SoftDeleteQuerySet)()

    def __str__(self):
        return self.subcategory

