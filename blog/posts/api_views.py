from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Topic, Category, Post
from .serializers import TopicSerializer


# określamy dostępne metody żądania dla tego endpointu
@api_view(['GET'])
def topic_list(request):
    """
    Lista wszystkich obiektów modelu Topic.
    """
    if request.method == 'GET':
        topics = Topic.objects.all()
        serializer = TopicSerializer(topics, many=True)
        return Response(serializer.data)
