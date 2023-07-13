from django.db import models
from django.contrib.auth.models import User

status = ((0, 'Unavailable'), (1, 'Available'))

MEAL_TYPE = (
    ('starters','Starters'),
    ('salads','Salad'),
    ('maindish', 'Main Dish'),
    ('desserts', 'Desserts')
)

class Item(models.Model):
    meal = models.CharField(max_length=1000, unique=True)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    meal_type = models.CharField(max_length=2000, choices=MEAL_TYPE)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.IntegerField(choices=status)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.meal

