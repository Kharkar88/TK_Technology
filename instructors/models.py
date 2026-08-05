from django.db import models

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=100)
    experience = models.PositiveIntegerField()
    image = models.ImageField(upload_to='instructors/')

    def __str__(self):
        return self.name