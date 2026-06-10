from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from kitchen.models import Dish, Cook, DishType
from django.shortcuts import render
from django.db.models import Avg
from django.views import generic
from .forms import CookCreationForm


def index(request):
    context = {
        "dish_count": Dish.objects.count(),
        "cook_count": Cook.objects.count(),
        "avg_price": Dish.objects.aggregate(Avg("price"))["price__avg"],
    }
    return render(request, "kitchen/index.html", context)


class RegisterView(generic.CreateView):
    form_class = CookCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("kitchen:index")


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
    success_url = reverse_lazy("kitchen:dish-list")


class DishUpdateView(UpdateView):
    model = Dish
    fields = ["name", "description", "price", "dish_type", "cooks"]
    template_name = "kitchen/dish_form.html"
    success_url = reverse_lazy("kitchen:dish-list")


class DishDeleteView(DeleteView):
    model = Dish
    template_name = "kitchen/dish_confirm_delete.html"
    success_url = reverse_lazy("kitchen:dish-list")


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
    success_url = reverse_lazy("kitchen:cook-list")


class CookUpdateView(UpdateView):
    model = Cook
    fields = ["username", "first_name", "last_name", "years_of_experience"]
    template_name = "kitchen/cook_form.html"
    success_url = reverse_lazy("kitchen:cook-list")


class CookDeleteView(DeleteView):
    model = Cook
    template_name = "kitchen/cook_confirm_delete.html"
    success_url = reverse_lazy("kitchen:cook-list")


class DishTypeListView(ListView):
    model = DishType
    template_name = "kitchen/dishtype_list.html"


class DishTypeDetailView(DetailView):
    model = DishType
    template_name = "kitchen/dishtype_detail.html"


class DishTypeCreateView(CreateView):
    model = DishType
    fields = ["name"]
    template_name = "kitchen/dishtype_form.html"
    success_url = reverse_lazy("kitchen:dishtype-list")


class DishTypeUpdateView(UpdateView):
    model = DishType
    fields = ["name"]
    template_name = "kitchen/dishtype_form.html"
    success_url = reverse_lazy("kitchen:dishtype-list")


class DishTypeDeleteView(DeleteView):
    model = DishType
    template_name = "kitchen/dishtype_confirm_delete.html"
    success_url = reverse_lazy("kitchen:dishtype-list")
