from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Welcome to Kitchen Home page</h1>")
