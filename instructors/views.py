from django.shortcuts import render

def add_instructor(request):
    return render(request, 'add_instructor.html')