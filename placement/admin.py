from django.contrib import admin
from .models import Placement


@admin.register(Placement)
class PlacementAdmin(admin.ModelAdmin):

    list_display = (
        "student_name",
        "company_name",
        "job_role",
        "package",
        "placement_date",
    )

    search_fields = (
        "student_name",
        "company_name",
        "job_role",
    )

    list_filter = (
        "company_name",
        "placement_date",
    )