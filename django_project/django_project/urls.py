from django.conf.urls import url, include
from django.contrib import admin
from tdiderich import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home),
    staticfiles_urlpatterns(),
]
