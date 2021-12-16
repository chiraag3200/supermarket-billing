from django.db import models
from djangodeletes.softdeletes import SoftDeletable, SoftDeleteQuerySet, SoftDeleteManager


# Create your models here.
class Category(SoftDeletable, models.Model):
    category = models.CharField(max_length=50, null=False, blank = False, unique = True)

    objects = SoftDeleteManager.from_queryset(SoftDeleteQuerySet)()

    def __str__(self):
        return self.category

