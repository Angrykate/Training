from django.shortcuts import render
from rest_framework import generics,permissions
from cahier.models import Course, Task
from cahier.serializers import CourseSerializer, TaskSerializer
from cahier.permissions import IsTeacher


class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated, IsTeacher]


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]


