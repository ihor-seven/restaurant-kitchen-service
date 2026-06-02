from django.urls import path
from django.contrib.auth import views as auth_views
from kitchen import views

app_name = "kitchen"

urlpatterns = [
    path("", views.index, name="index"),
    path("dishes/", views.DishListView.as_view(), name="dish-list"),
    path(
        "dishes/<int:pk>/",
        views.DishDetailView.as_view(),
        name="dish-detail",
    ),
    path("dishes/create/", views.DishCreateView.as_view(), name="dish-create"),
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
    path("cooks/", views.CookListView.as_view(), name="cook-list"),
    path(
        "cooks/<int:pk>/",
        views.CookDetailView.as_view(),
        name="cook-detail",
    ),
    path("cooks/create/", views.CookCreateView.as_view(), name="cook-create"),
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
    path(
        "dish-types/",
        views.DishTypeListView.as_view(),
        name="dishtype-list"
    ),
    path(
        "dish-types/<int:pk>/",
        views.DishTypeDetailView.as_view(),
        name="dishtype-detail",
    ),
    path(
        "dish-types/create/",
        views.DishTypeCreateView.as_view(),
        name="dishtype-create",
    ),
    path(
        "dish-types/<int:pk>/update/",
        views.DishTypeUpdateView.as_view(),
        name="dishtype-update",
    ),
    path(
        "dish-types/<int:pk>/delete/",
        views.DishTypeDeleteView.as_view(),
        name="dishtype-delete",
    ),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="registration/login.html"
        ),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
