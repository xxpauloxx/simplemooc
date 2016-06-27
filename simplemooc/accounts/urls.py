from django.conf.urls import url
from django.contrib.auth import views as accounts_views
from simplemooc.accounts import views


urlpatterns = [
    url(r'^entrar/$', accounts_views.login,
        {'template_name': 'accounts/login.html'}, name='login'),

    url(r'^sair/$', accounts_views.logout,
        {'next_page': 'core:home'}, name='logout'),

    url(r'^cadastre-se/$', views.register, name='register'),
]
