from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'course', 'created_at')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('course', 'created_at')