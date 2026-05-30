from django.test import TestCase
from django.urls import reverse
from kitchen.models import Dish, DishType, Cook


class DishModelTest(TestCase):
    def test_create_dish(self):
        dish_type = DishType.objects.create(name="Soup")
        dish = Dish.objects.create(
            name="Borshch",
            description="Traditional soup",
            price=120,
            dish_type=dish_type
        )
        self.assertEqual(dish.name, "Borshch")
        self.assertEqual(str(dish), "Borshch")


class CookModelTest(TestCase):
    def test_create_cook(self):
        cook = Cook.objects.create(
            first_name="Ivan",
            last_name="Petrenko",
            username="ivanpetrenko"
        )
        self.assertEqual(str(cook), "Ivan Petrenko")


class DashboardViewTest(TestCase):
    def test_dashboard_page(self):
        url = reverse("kitchen:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Kitchen Dashboard")
