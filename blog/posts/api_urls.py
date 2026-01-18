from django.urls import path, include
from . import api_views

urlpatterns = [
    path('topics/', api_views.topic_list),
    path('topics/<int:pk>/', api_views.topic_detail),
    path('topics/create/', api_views.topic_create),
    path('topics/find/<str:phrase>', api_views.topic_by_name),
]