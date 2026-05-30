from django.shortcuts import render
from django.views import generic
from .models import Dish, Cook

def index(request):
    return render(request, "kitchen/index.html")

class DishListView(generic.ListView):
    model = Dish
    template_name = "kitchen/dish_list.html"

class DishDetailView(generic.DetailView):
    model = Dish
    template_name = "kitchen/dish_detail.html"

class CookListView(generic.ListView):
    model = Cook
    template_name = "kitchen/cook_list.html"

class CookDetailView(generic.DetailView):
    model = Cook
    template_name = "kitchen/cook_detail.html"
