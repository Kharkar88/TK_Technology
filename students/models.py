from django.db import models
from courses.models import Course

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    date_of_birth = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='students/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name