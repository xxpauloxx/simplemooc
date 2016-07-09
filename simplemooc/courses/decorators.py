from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from django.contrib import messages

from .models import Course, Enrollment


def enrollment_required(view_func):
    def _wrapper(request, *args, **kwargs):
        slug = kwargs['slug']
        course = get_object_or_404(Course, slug=slug)
        has_permission = request.user.is_staff

        if not has_permission:
            try:
                enrollment = Enrollment.objects.get(
                    user=request.user, course=course
                )
            except Enrollment.DoesNotExist:
                message = '''Desculpe, mas você não tem permissão para
                             acessar esta página'''
            else:
                if enrollment.is_approved():
                    has_permission = True
                else:
                    message = 'A sua inscrição no curso ainda está pendente'

        if not has_permission:
            messages.error(request, message)
            return redirect('accounts:dashboard')

        request.course = course
        return view_func(request, *args, **kwargs)

    return _wrapper
