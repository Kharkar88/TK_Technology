from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path(
        'admin/',
        admin.site.urls
    ),

    path(
        '',
        include('dashboard.urls')
    ),

    path(
        'courses/',
        include('courses.urls')
    ),

    path(
        'students/',
        include('students.urls')
    ),

    path(
        'contact/',
        include('contact.urls')
    ),

    path(
        'payments/',
        include('payments.urls')
    ),

    path(
        'certificates/',
        include('certificates.urls')
    ),

    path(
        'adminpanel/',
        include('adminpanel.urls')
    ),

    path(
        'feedback/',
        include('feedback.urls')
    ),

    path(
        'placements/',
        include('placement.urls')
    ),

    path(
        'attendance/',
        include('attendance.urls')
    ),

    path(
        'results/',
        include('results.urls')
    ),
    path(
        'instructors/', 
        include('instructors.urls')),

]

if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )