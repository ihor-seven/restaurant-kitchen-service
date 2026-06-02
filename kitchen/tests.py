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
            username="ivanpetrenko",
            years_of_experience=3
        )
        self.assertEqual(str(cook), "Ivan Petrenko")


class DashboardViewTest(TestCase):
    def test_dashboard_page(self):
        url = reverse("kitchen:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Kitchen Dashboard")


class DishCRUDTest(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(name="Soup")
        self.cook = Cook.objects.create(
            first_name="Ivan",
            last_name="Petrenko",
            username="ivanpetrenko",
            years_of_experience=3
        )
        self.dish = Dish.objects.create(
            name="Test Dish",
            description="Test description",
            price=100,
            dish_type=self.dish_type
        )
        self.dish.cooks.add(self.cook)

    def test_dish_list_view(self):
        url = reverse("kitchen:dish-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Dish")

    def test_dish_detail_view(self):
        url = reverse("kitchen:dish-detail", args=[self.dish.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test description")

    def test_dish_create_view(self):
        url = reverse("kitchen:dish-create")
        response = self.client.post(url, {
            "name": "New Dish",
            "description": "New description",
            "price": 150,
            "dish_type": self.dish_type.id,
            "cooks": [self.cook.id]
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Dish.objects.filter(name="New Dish").exists())

    def test_dish_update_view(self):
        url = reverse("kitchen:dish-update", args=[self.dish.id])
        response = self.client.post(url, {
            "name": "Updated Dish",
            "description": "Updated description",
            "price": 200,
            "dish_type": self.dish_type.id,
            "cooks": [self.cook.id]
        })
        self.assertEqual(response.status_code, 302)
        self.dish.refresh_from_db()
        self.assertEqual(self.dish.name, "Updated Dish")

    def test_dish_delete_view(self):
        url = reverse("kitchen:dish-delete", args=[self.dish.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Dish.objects.filter(id=self.dish.id).exists())
