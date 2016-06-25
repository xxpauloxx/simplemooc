from django.conf.urls import url
from simplemooc.core import views as core_views


urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    url(r'^contato/$', core_views.contact, name='contact'),
]
