from django.conf.urls import url
from simplemooc.courses import views as courses_views


urlpatterns = [
    url(r'^$', courses_views.index, name='index'),
    url(r'^(?P<slug>[\w_-]+)/$', courses_views.details, name='details'),
    
    url(r'^(?P<slug>[\w_-]+)/inscricao/$', 
        courses_views.enrollment, name='enrollment'),

    url(r'^(?P<slug>[\w_-]+)/cancelar-inscricao/$', 
        courses_views.undo_enrollment, name='undo_enrollment'),

    url(r'^(?P<slug>[\w_-]+)/anuncios/$', 
        courses_views.announcements, name='announcements'),
]
