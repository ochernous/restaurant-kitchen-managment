from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from kitchen.models import Cook, Dish, DishType


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    search_fields = ("name", )


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "dish_type", )
    list_filter = ("dish_type", )
    search_fields = ("name", )


@admin.register(Cook)
class CookAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience", )
    fieldsets = UserAdmin.fieldsets + (
        ("Additional information", {"fields": ("years_of_experience", )}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional information", {"fields": (
            "first_name", "last_name", "email", "years_of_experience",
        )}),
    )
