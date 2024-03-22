from django.shortcuts import render
from django.http import HttpResponse

from goods.models import Categories

def index(request):

    categjries = Categories.objects
    context: dict = {
        "title": "Home - главная",
        "content": "Магазин мебели HOME"

    }

    return render(request,"main/index.html", context)

def about(request):
    context: dict = {
        "title": "Home - О нас",
        "content": "О нас",
        "text_on_page": "Текст о том почему этот магазин такой классный, и какой хороший товар"
    }

    return render(request, "main/about.html", context)