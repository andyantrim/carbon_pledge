from django.shortcuts import render

# Create your views here.

from tasks.models import Tasks
from rest_framework import viewsets
from tasks.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint to view or edit Tasks
    """
    queryset = Tasks.objects.filter(active=True)
    serializer_class = TaskSerializer
