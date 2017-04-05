from django.conf.urls import url, include
from django.contrib import admin
from tdiderich import views
from django.conf.urls.static import static
from django.conf import settings

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home),
    url(r'^about/', views.about, name='about'),
    url(r'^contact/', views.contact, name='contact')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
