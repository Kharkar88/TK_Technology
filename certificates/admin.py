from django.contrib import admin
from .models import Certificate


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'student',
        'course',
        'certificate_number',
        'issue_date',
    )

    search_fields = (
        'student__name',
        'student__email',
        'certificate_number',
    )

    list_filter = (
        'course',
        'issue_date',
    )

    ordering = (
        '-issue_date',
    )