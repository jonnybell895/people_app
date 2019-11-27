from django.db import models


class People(models.Model):
    """
    People Model

    Defines database model and constraints for fields
    """
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120, unique=True)
    age = models.PositiveIntegerField()
    balance = models.FloatField()
    address = models.CharField(max_length=200)

    class Meta:
        ordering = ["name", "email"]  # Allow order by name or email
