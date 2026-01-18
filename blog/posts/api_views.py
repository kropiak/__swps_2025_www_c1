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


@api_view(['GET', 'PUT', 'DELETE'])
def topic_detail(request, pk):
    """
    :param request: obiekt DRF Request
    :param pk: id obiektu Topic
    :return: Response (with status and/or object/s data)
    """
    try:
        topic = Topic.objects.get(pk=pk)
    except Topic.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    """
    Zwraca pojedynczy obiekt typu Topic.
    """
    if request.method == 'GET':
        topic = Topic.objects.get(pk=pk)
        serializer = TopicSerializer(topic)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TopicSerializer(topic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        topic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def topic_create(request):
    serializer = TopicSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
