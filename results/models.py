from django.db import models
from students.models import Student
from courses.models import Course


class Result(models.Model):

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    theory_marks = models.PositiveIntegerField()

    practical_marks = models.PositiveIntegerField()

    total_marks = models.PositiveIntegerField(
        editable=False
    )

    percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        editable=False
    )

    grade = models.CharField(
        max_length=5,
        editable=False
    )

    result = models.CharField(
        max_length=10,
        editable=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def save(self, *args, **kwargs):

        self.total_marks = self.theory_marks + self.practical_marks

        self.percentage = self.total_marks / 2

        if self.percentage >= 90:
            self.grade = "A+"

        elif self.percentage >= 80:
            self.grade = "A"

        elif self.percentage >= 70:
            self.grade = "B"

        elif self.percentage >= 60:
            self.grade = "C"

        elif self.percentage >= 40:
            self.grade = "D"

        else:
            self.grade = "F"

        if self.percentage >= 40:
            self.result = "Pass"
        else:
            self.result = "Fail"

        super().save(*args, **kwargs)

    def __str__(self):

        return f"{self.student.name} - {self.course.name}"