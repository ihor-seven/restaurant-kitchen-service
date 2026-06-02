from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from kitchen.models import Dish, Cook
from django.shortcuts import render

def index(request):
    return render(request, "kitchen/index.html")

class DishListView(ListView):
    model = Dish
    template_name = "kitchen/dish_list.html"


class DishDetailView(DetailView):
    model = Dish
    template_name = "kitchen/dish_detail.html"


class DishCreateView(CreateView):
    model = Dish
    fields = ["name", "description", "price", "dish_type", "cooks"]
    template_name = "kitchen/dish_form.html"
    success_url = reverse_lazy("dish-list")


class DishUpdateView(UpdateView):
    model = Dish
    fields = ["name", "description", "price", "dish_type", "cooks"]
    template_name = "kitchen/dish_form.html"
    success_url = reverse_lazy("dish-list")


class DishDeleteView(DeleteView):
    model = Dish
    template_name = "kitchen/dish_confirm_delete.html"
    success_url = reverse_lazy("dish-list")


class CookListView(ListView):
    model = Cook
    template_name = "kitchen/cook_list.html"


class CookDetailView(DetailView):
    model = Cook
    template_name = "kitchen/cook_detail.html"


class CookCreateView(CreateView):
    model = Cook
    fields = ["username", "first_name", "last_name", "years_of_experience"]
    template_name = "kitchen/cook_form.html"
    success_url = reverse_lazy("cook-list")


class CookUpdateView(UpdateView):
    model = Cook
    fields = ["username", "first_name", "last_name", "years_of_experience"]
    template_name = "kitchen/cook_form.html"
    success_url = reverse_lazy("cook-list")


class CookDeleteView(DeleteView):
    model = Cook
    template_name = "kitchen/cook_confirm_delete.html"
    success_url = reverse_lazy("cook-list")
