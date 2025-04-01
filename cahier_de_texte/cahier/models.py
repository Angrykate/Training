from django.db import models


# Create your models here.
class Course(models.Model):


    def __str__(self):
        return f'{self.title}'

    title = models.fields.CharField(max_length=100)
    course_code = models.fields.CharField(max_length=10)
    description = models.fields.TextField()
    created_at = models.fields.DateTimeField()

class Task(models.Model):

    title = models.fields.CharField(max_length=100)
    due_date = models.fields.DateTimeField()
    description = models.fields.TextField()
    course = models.ForeignKey(Course, related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.title