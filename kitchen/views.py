from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from kitchen.models import Cook, Dish, DishType


def index(request: HttpRequest) -> HttpResponse:
    context = {
        "num_cooks": Cook.objects.count(),
        "num_dishes": Dish.objects.count(),
        "num_dishtypes": DishType.objects.count()
    }
    return render(request, "kitchen/index.html", context=context)
