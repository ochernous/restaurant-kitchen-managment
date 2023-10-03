from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField

from kitchen.models import Cook, Dish


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "first_name", "last_name", "email", "years_of_experience"
        )


class CookUpdateForm(UserChangeForm):
    password = ReadOnlyPasswordHashField(
        label="Password",
        help_text=(
            "Raw passwords are not stored, so there is no way to see this "
            "user’s password"
        ),
    )

    class Meta:
        model = Cook
        fields = (
            "email", "years_of_experience"
        )

    def save(self, commit=True):
        cook = super().save(commit=False)
        email = self.cleaned_data.get("email")
        years_of_experience = self.cleaned_data.get("years_of_experience")
        cook.email = email
        cook.years_of_experience = years_of_experience
        if commit:
            cook.save()
        return cook


class DishForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Dish
        fields = "__all__"


class DishTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "search by name"})
    )


class DishSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "search by name"})
    )


class CookSearchForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "search by username"})
    )
