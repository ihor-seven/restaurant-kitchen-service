from django.urls import path
from kitchen import views

app_name = "kitchen"

urlpatterns = [
    # Index
    path("", views.index, name="index"),

    path(
        "dishes/",
        views.DishListView.as_view(),
        name="dish-list",
    ),
    path(
        "dishes/<int:pk>/",
        views.DishDetailView.as_view(),
        name="dish-detail",
    ),
    path(
        "dishes/create/",
        views.DishCreateView.as_view(),
        name="dish-create",
    ),
    path(
        "dishes/<int:pk>/update/",
        views.DishUpdateView.as_view(),
        name="dish-update",
    ),
    path(
        "dishes/<int:pk>/delete/",
        views.DishDeleteView.as_view(),
        name="dish-delete",
    ),

    # ---------- Cook CRUD ----------
    path(
        "cooks/",
        views.CookListView.as_view(),
        name="cook-list",
    ),
    path(
        "cooks/<int:pk>/",
        views.CookDetailView.as_view(),
        name="cook-detail",
    ),
    path(
        "cooks/create/",
        views.CookCreateView.as_view(),
        name="cook-create",
    ),
    path(
        "cooks/<int:pk>/update/",
        views.CookUpdateView.as_view(),
        name="cook-update",
    ),
    path(
        "cooks/<int:pk>/delete/",
        views.CookDeleteView.as_view(),
        name="cook-delete",
    ),
]
