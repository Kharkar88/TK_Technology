from django.db import models
from students.models import Student
from courses.models import Course


class Certificate(models.Model):

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    certificate_number = models.CharField(
        max_length=50,
        unique=True
    )

    issue_date = models.DateField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.student.name} - {self.course.name}"