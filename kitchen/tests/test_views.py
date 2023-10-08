from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import DishType, Dish, Cook

DISH_TYPE_URL = reverse("kitchen:dish-type-list")
DISH_URL = reverse("kitchen:dish-list")
COOK_URL = reverse("kitchen:cook-list")


class PublicDishTypeTest(TestCase):
    def test_login_required(self):
        resp = self.client.get(DISH_TYPE_URL)
        self.assertNotEquals(resp.status_code, 200)

class PrivateDishTypeTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test_username",
            password="12test_password34",
        )
        self.client.force_login(self.user)
        self.dish_type1 = DishType.objects.create(name="seafood")
        self.dish_type2 = DishType.objects.create(name="cake")

    def test_retrieve_dish_types(self):
        resp = self.client.get(DISH_TYPE_URL)
        self.assertEquals(resp.status_code, 200)
        dish_types = DishType.objects.all()
        self.assertEquals(
            list(resp.context["dish_type_list"]), list(dish_types)
        )
        self.assertTemplateUsed(resp, "kitchen/dish_type_list.html")

    def test_search_dish_types(self):
        resp = self.client.get(DISH_TYPE_URL, {"name": "seafood"})
        self.assertEquals(list(resp.context["dish_type_list"]), [self.dish_type1])

class PublicDishTest(TestCase):
    def test_login_required(self):
        resp = self.client.get(DISH_URL)
        self.assertNotEquals(resp.status_code, 200)


class PrivateDishTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test_username",
            password="12testpassword34",
        )
        self.client.force_login(self.user)
        dish_type = DishType.objects.create(name="salad")
        self.dish1 = Dish.objects.create(
            name="Cesar",
            description="The Cesar Salad is the best",
            price=11.11,
            dish_type=dish_type,
        )
        self.dish2 = Dish.objects.create(
            name="Esqueixada",
            description="The Esqueixada Salad is the best",
            price=12.51,
            dish_type=dish_type,
        )

    def test_retrieve_dishes(self):
        resp = self.client.get(DISH_URL)
        self.assertEquals(resp.status_code, 200)
        dishes = Dish.objects.all()
        self.assertEquals(
            list(resp.context["dish_list"]), list(dishes)
        )
        self.assertTemplateUsed(resp, "kitchen/dish_list.html")

    def test_search_dishes(self):
        resp = self.client.get(DISH_URL, {"name": "Cesar"})
        self.assertEquals(list(resp.context["dish_list"]), [self.dish1])


class PublicCookTest(TestCase):
    def test_login_required(self):
        resp = self.client.get(COOK_URL)
        self.assertNotEquals(resp.status_code, 200)


class PrivateCookTest(TestCase):
    def setUp(self):
        self.user1 = get_user_model().objects.create_user(
            username="test_username1",
            password="12password341",
        )
        self.client.force_login(self.user1)
        self.user2 = get_user_model().objects.create_user(
            username="test_username2",
            password="12password342",
        )

    def test_retrieve_users(self):
        resp = self.client.get(COOK_URL)
        self.assertEquals(resp.status_code, 200)
        users = Cook.objects.all()
        self.assertEquals(
            list(resp.context["cook_list"]), list(users)
        )
        self.assertTemplateUsed(resp, "kitchen/cook_list.html")

    def test_search_users(self):
        resp = self.client.get(COOK_URL, {"username": "test_username1"})
        self.assertEquals(list(resp.context["cook_list"]), [self.user1])

    def test_create_cook(self):
        form_data = {
            "username": "new_user",
            "password1": "12pass34word",
            "password2": "12pass34word",
            "first_name": "Name",
            "last_name": "Surname",
            "email": "user@mail.com",
            "years_of_experience": 3
        }
        self.client.post(reverse("kitchen:cook-create"), data=form_data)
        new_user = get_user_model().objects.get(username=form_data["username"])

        self.assertEquals(new_user.first_name, form_data["first_name"])
        self.assertEquals(new_user.last_name, form_data["last_name"])
        self.assertEquals(new_user.email, form_data["email"])
        self.assertEquals(new_user.years_of_experience, form_data["years_of_experience"])
