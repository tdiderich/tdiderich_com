from django.conf.urls import url, include
from django.contrib import admin
from tdiderich import views

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home),
]
