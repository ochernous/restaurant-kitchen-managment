from django.test import TestCase

from kitchen.forms import CookCreationForm


class FormsTests(TestCase):
    def test_cook_creation_form_with_first_last_name_email_experience_is_valid(
        self,
    ):
        form_data = {
            "username": "new_user",
            "password1": "12pass34word",
            "password2": "12pass34word",
            "first_name": "Name",
            "last_name": "Surname",
            "email": "user@mail.com",
            "years_of_experience": 3,
        }
        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEquals(form.cleaned_data, form_data)
