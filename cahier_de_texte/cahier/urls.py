from django.urls import path
from cahier.views import CourseListCreateView,TaskListCreateView


urlpatterns = [
    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create')
]
