from django.shortcuts import render, get_object_or_404
from .models import Course


def index(request):
    courses = Course.objects.all()
    template_name = 'courses/index.html'
    context = {'courses': courses}

    return render(request, template_name, context)


def details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    context = {'course': course}

    template_name = 'courses/details.html'
    return render(request, template_name, context)
