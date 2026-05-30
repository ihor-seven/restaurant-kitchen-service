from django.contrib import admin
from .models import DishType, Dish, Cook, Ingredient


admin.site.register(DishType)
admin.site.register(Dish)
admin.site.register(Cook)
admin.site.register(Ingredient)
