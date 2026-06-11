from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from django.shortcuts import render
from django.db.models import Avg
from .models import Dish, Cook, DishType
from .forms import CookCreationForm


def index(request):
    context = {
        "dish_count": Dish.objects.count(),
        "cook_count": Cook.objects.count(),
        "avg_price": Dish.objects.aggregate(Avg("price"))["price__avg"] or 0,
    }
    return render(request, "kitchen/index.html", context)


class RegisterView(CreateView):
    form_class = CookCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("kitchen:index")

    def form_valid(self, form):
        response = super().form_valid(form)
        # автоматичний логін після реєстрації
        login(self.request, self.object)
        return response


class DishListView(ListView):
    model = Dish
    template_name = "kitchen/dish_list.html"


class DishDetailView(DetailView):
    model = Dish
    template_name = "kitchen/dish_detail.html"


class DishCreateView(LoginRequiredMixin, CreateView):
    model = Dish
    fields = ["name", "description", "price", "dish_type", "cooks"]
    template_name = "kitchen/dish_form.html"
    success_url = reverse_lazy("kitchen:dish-list")


class DishUpdateView(LoginRequiredMixin, UpdateView):
    model = Dish
    fields = ["name", "description", "price", "dish_type", "cooks"]
    template_name = "kitchen/dish_form.html"
    success_url = reverse_lazy("kitchen:dish-list")


class DishDeleteView(LoginRequiredMixin, DeleteView):
    model = Dish
    template_name = "kitchen/dish_confirm_delete.html"
    success_url = reverse_lazy("kitchen:dish-list")


class CookListView(ListView):
    model = Cook
    template_name = "kitchen/cook_list.html"


class CookDetailView(DetailView):
    model = Cook
    template_name = "kitchen/cook_detail.html"


class CookCreateView(LoginRequiredMixin, CreateView):
    model = Cook
    fields = ["username", "first_name", "last_name", "years_of_experience"]
    template_name = "kitchen/cook_form.html"
    success_url = reverse_lazy("kitchen:cook-list")


class CookUpdateView(LoginRequiredMixin, UpdateView):
    model = Cook
    fields = ["username", "first_name", "last_name", "years_of_experience"]
    template_name = "kitchen/cook_form.html"
    success_url = reverse_lazy("kitchen:cook-list")


class CookDeleteView(LoginRequiredMixin, DeleteView):
    model = Cook
    template_name = "kitchen/cook_confirm_delete.html"
    success_url = reverse_lazy("kitchen:cook-list")


class DishTypeListView(ListView):
    model = DishType
    template_name = "kitchen/dishtype_list.html"


class DishTypeDetailView(DetailView):
    model = DishType
    template_name = "kitchen/dishtype_detail.html"


class DishTypeCreateView(LoginRequiredMixin, CreateView):
    model = DishType
    fields = ["name"]
    template_name = "kitchen/dishtype_form.html"
    success_url = reverse_lazy("kitchen:dishtype-list")


class DishTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = DishType
    fields = ["name"]
    template_name = "kitchen/dishtype_form.html"
    success_url = reverse_lazy("kitchen:dishtype-list")


class DishTypeDeleteView(LoginRequiredMixin, DeleteView):
    model = DishType
    template_name = "kitchen/dishtype_confirm_delete.html"
    success_url = reverse_lazy("kitchen:dishtype-list")
