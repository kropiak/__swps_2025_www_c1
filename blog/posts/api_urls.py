from django.urls import path, include
from . import api_views

urlpatterns = [
    path('topics/', api_views.topic_list),
    # path('persons/<int:pk>/', api_views.person_detail),
]