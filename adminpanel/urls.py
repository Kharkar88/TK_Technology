from django.urls import path

from .views.dashboard import admin_dashboard

from .views.students import (
    student_management,
    edit_student,
    delete_student,
)

from .views.courses import (
    course_management,
    edit_course,
    delete_course,
)

from .views.trainers import (
    trainer_management,
    edit_trainer,
    delete_trainer,
)

from .views.payments import (
    payment_management,
    edit_payment,
    delete_payment,
)

from .views.contacts import (
    contact_management,
    contact_detail,
    delete_contact,
)

from .views.certificates import (
    certificate_management,
    certificate_detail,
    delete_certificate,
)

from .views.placements import (
    placement_management,
    add_placement,
    edit_placement,
    delete_placement,
)

from .views.attendance import (
    attendance_management,
    add_attendance,
    edit_attendance,
    delete_attendance,
)

from .views.results import (
    result_management,
    add_result,
    edit_result,
    delete_result,
)

urlpatterns = [

    path("", admin_dashboard, name="admin_dashboard"),

    # Students
    path("students/", student_management, name="student_management"),
    path("students/edit/<int:student_id>/", edit_student, name="edit_student"),
    path("students/delete/<int:student_id>/", delete_student, name="delete_student"),

    # Courses
    path("courses/", course_management, name="course_management"),
    path("courses/edit/<int:course_id>/", edit_course, name="edit_course"),
    path("courses/delete/<int:course_id>/", delete_course, name="delete_course"),

    # Trainers
    path("trainers/", trainer_management, name="trainer_management"),
    path("trainers/edit/<int:trainer_id>/", edit_trainer, name="edit_trainer"),
    path("trainers/delete/<int:trainer_id>/", delete_trainer, name="delete_trainer"),

    # Payments
    path("payments/", payment_management, name="payment_management"),
    path("payments/edit/<int:payment_id>/", edit_payment, name="edit_payment"),
    path("payments/delete/<int:payment_id>/", delete_payment, name="delete_payment"),

    # Certificates
    path("certificates/", certificate_management, name="certificate_management"),
    path("certificates/<int:certificate_id>/", certificate_detail, name="certificate_detail"),
    path("certificates/delete/<int:certificate_id>/", delete_certificate, name="delete_certificate"),

    # Placements
    path("placements/", placement_management, name="placement_management"),
    path("placements/add/", add_placement, name="add_placement"),
    path("placements/edit/<int:placement_id>/", edit_placement, name="edit_placement"),
    path("placements/delete/<int:placement_id>/", delete_placement, name="delete_placement"),

    # Attendance
    path("attendance/", attendance_management, name="attendance_management"),
    path("attendance/add/", add_attendance, name="add_attendance"),
    path("attendance/edit/<int:attendance_id>/", edit_attendance, name="edit_attendance"),
    path("attendance/delete/<int:attendance_id>/", delete_attendance, name="delete_attendance"),

    # Results
    path("results/", result_management, name="result_management"),
    path("results/add/", add_result, name="add_result"),
    path("results/edit/<int:result_id>/", edit_result, name="edit_result"),
    path("results/delete/<int:result_id>/", delete_result, name="delete_result"),

    # Contacts
    path("contacts/", contact_management, name="contact_management"),
    path("contacts/<int:contact_id>/", contact_detail, name="contact_detail"),
    path("contacts/delete/<int:contact_id>/", delete_contact, name="delete_contact"),

]