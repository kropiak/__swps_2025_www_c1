from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Topic, Category


def welcome_view(request):
    now = datetime.datetime.now()
    html = f"""
        <html><body>
        Witaj użytkowniku! </br>
        Aktualna data i czas na serwerze: {now}.
        </body></html>"""
    return HttpResponse(html)


def topic_list(request):
    # pobieramy wszystkie obiekty Topic z bazy poprzez QuerySet
    topics = Topic.objects.all()
    return HttpResponse(topics)


def category_list(request):
    # pobieramy wszystkie obiekty Category z bazy poprzez QuerySet
    categories = Category.objects.all()

    return render(request,
                  "posts/category/list.html",
                  {'categories': categories})


def category_detail(request, id):
    # pobieramy konkretny obiekt Category
    category = Category.objects.get(id=id)

    return render(request,
                  "posts/category/detail.html",
                  {'category': category})