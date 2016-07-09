from django.conf.urls import url
from simplemooc.forum import views as forum_views


urlpatterns = [
    url(r'^$', forum_views.index, name='index'),
    url(r'^tag/(?P<tag>[\w_-]+)/$', forum_views.index, name='index_tagged'),

    url(r'^respostas/(?P<pk>\d+)/correta/$', forum_views.reply_correct,
        name='reply_correct'),

    url(r'^respostas/(?P<pk>\d+)/incorreta/$', forum_views.reply_incorrect,
        name='reply_incorrect'),

    url(r'^(?P<slug>[\w_-]+)/$', forum_views.thread, name='thread'),
]
