from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'mep_django.linkedin.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/$', 'mep_django.linkedin.views.logout', name='logout'),
    url(r'^about/$', 'mep_django.linkedin.views.about', name='about'),
    url(r'^contact/$', 'mep_django.linkedin.views.contact', name='contact'),
    url(r'^profile/$', 'mep_django.linkedin.views.profile', name='profile'),
    url(r'^news/$', 'mep_django.linkedin.views.news', name='news'),
    url('', include('social.apps.django_app.urls', namespace='social')),
)

