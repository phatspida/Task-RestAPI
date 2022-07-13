from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Task
from .serializers import TaskSerializer

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/task-list/',
        'Detail View':'/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def apitasklist(request):
    list = Task.objects.all()
    serialized = TaskSerializer(list, many = True)
    return Response(serialized.data)

# CREATE
@api_view(['POST'])
def apitaskcreate(request):
    serialized = TaskSerializer(data = request.data)
    if serialized.is_valid():
        serialized.save()
    return Response(serialized.data)

# READ
@api_view(['GET'])
def apitaskdetail(request, pk):
    list = Task.objects.get(id = pk)
    serialized = TaskSerializer(list, many = False)
    return Response(serialized.data)

# UPDATE
@api_view(['POST'])
def apitaskupdate(request, pk):
    data = Task.objects.get(id = pk)
    serialized = TaskSerializer(instance = data, data = request.data)
    if serialized.is_valid():
        serialized.save()
    return Response(serialized.data)

# DELETE
@api_view(['DELETE'])
def apitaskdelete(request, pk):
    data = Task.objects.get(id = pk)
    data.delete()
    return Response('Item successfully deleted')
