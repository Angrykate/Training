from rest_framework.serializers import ModelSerializer

from cahier.models import Course,Task

class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
