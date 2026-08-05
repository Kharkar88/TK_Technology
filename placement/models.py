from django.db import models


class Placement(models.Model):

    student_name = models.CharField(
        max_length=100
    )

    company_name = models.CharField(
        max_length=100
    )

    job_role = models.CharField(
        max_length=100
    )

    package = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    placement_date = models.DateField()

    company_logo = models.ImageField(
        upload_to="placements/"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"{self.student_name} - {self.company_name}"