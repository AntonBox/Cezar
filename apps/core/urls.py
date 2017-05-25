from django.conf.urls import url
from apps.core import views as core_views


urlpatterns = [
    url(r'^$', core_views.cezar, name='contact'),
    url(r'^code/$', core_views.code, name='code'),
    url(r'^uncode/$', core_views.uncode, name='uncode')
]
