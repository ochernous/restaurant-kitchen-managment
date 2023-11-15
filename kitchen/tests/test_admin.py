from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="12adminpassword34",
        )
        self.client.force_login(self.admin_user)
        self.cook = get_user_model().objects.create_user(
            username="cook_user",
            password="cook_password",
            years_of_experience=9753,
        )

    def test_cook_years_of_experience_listed(self):
        """
        Test that cook's years_of_experience is in list_display on cook admin page
        :return:
        """
        url = reverse("admin:kitchen_cook_changelist")
        resp = self.client.get(url)
        self.assertContains(resp, self.cook.years_of_experience)

    def test_cook_detail_years_of_experience(self):
        """
        Test that cook's years_of_experience is on cook detail admin page
        :return:
        """
        url = reverse("admin:kitchen_cook_change", args=[self.cook.id])
        resp = self.client.get(url)
        self.assertContains(resp, self.cook.years_of_experience)

    def test_cook_add_fieldsets_years_of_experience_included(self):
        """
        Test that cook's years_of_experience is included in add_fields
        :return:
        """
        url = reverse("admin:kitchen_cook_add")
        resp = self.client.get(url)
        self.assertContains(resp, "years_of_experience")
