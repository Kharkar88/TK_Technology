from django.contrib import admin
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'student',
        'course',
        'amount',
        'payment_date',
        'transaction_id',
        'status',
    )

    list_filter = (
        'status',
        'payment_date',
        'course',
    )

    search_fields = (
        'student__name',
        'student__email',
        'transaction_id',
    )

    ordering = (
        '-payment_date',
    )