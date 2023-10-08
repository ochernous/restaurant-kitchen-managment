from django.contrib.auth import get_user_model
from django.test import TestCase

from kitchen.models import DishType, Dish


class ModelsTests(TestCase):
    def test_dish_type_str(self):
        dish_type = DishType.objects.create(name="test_dish_type")
        self.assertEquals(str(dish_type), dish_type.name)

    def test_cook_str(self):
        cook = get_user_model().objects.create(
            username="test_user",
            password="12test34",
            first_name="test_first",
            last_name="test_last",
        )
        self.assertEquals(
            str(cook), f"{cook.username}: {cook.first_name} {cook.last_name}"
        )

    def test_dish_str(self):
        dish_type = DishType.objects.create(name="test_dish_type")
        dish = Dish.objects.create(
            name="Test_dish",
            description="Test_dish - is the best test_dish",
            price=11.99,
            dish_type=dish_type,
        )
        self.assertEquals(
            str(dish),
            f"{dish.name}: price - {dish.price} ({dish.dish_type.name})",
        )

    def test_create_user_with_years_of_experience(self):
        username = "test_user"
        password = "12test34"
        years_of_experience = 5
        cook = get_user_model().objects.create_user(
            username=username,
            password=password,
            years_of_experience=years_of_experience,
        )
        self.assertEquals(cook.username, username)
        self.assertEquals(cook.years_of_experience, years_of_experience)
        self.assertTrue(cook.check_password(password))
