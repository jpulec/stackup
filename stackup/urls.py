from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from stackup.apps.main.views import Home, Salary, About

urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name="home"),
    url(r'^salary/$', Salary.as_view(), name="salary"),
    url(r'^about/$', About.as_view(), name="about"),
    url(r'^admin/', include(admin.site.urls)),
)
