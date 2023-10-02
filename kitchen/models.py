from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ("name", )

    def __str__(self) -> str:
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ("username", )

    def __str__(self) -> str:
        return f"{self.username}: {self.first_name} {self.last_name}"


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    dish_type = models.ForeignKey(
        DishType,
        on_delete=models.CASCADE,
        related_name="dishes"
    )
    cooks = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="dishes"
    )

    class Meta:
        ordering = ("name", )
        verbose_name_plural = "dishes"

    def __str__(self) -> str:
        return f"{self.name}: price - {self.price} ({self.dish_type.name})"
