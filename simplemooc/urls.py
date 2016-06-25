from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^', include('simplemooc.core.urls', namespace='core')),
    url(r'^cursos/', include('simplemooc.courses.urls', namespace='courses')),
    url(r'^admin/', admin.site.urls),
]
