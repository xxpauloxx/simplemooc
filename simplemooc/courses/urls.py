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

    url(r'^(?P<slug>[\w_-]+)/anuncios/(?P<pk>\d+)/$', 
        courses_views.show_announcement, name='show_announcement'),

    url(r'^(?P<slug>[\w_-]+)/aulas/$', courses_views.lessons, name='lessons'),
    
    url(r'^(?P<slug>[\w_-]+)/aulas/(?P<pk>\d+)/$', 
        courses_views.lesson, name='lesson'),

    url(r'^(?P<slug>[\w_-]+)/materiais/(?P<pk>\d+)/$', 
        courses_views.material, name='material'),

]
