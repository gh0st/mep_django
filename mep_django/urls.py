from django.conf.urls import patterns, include, url
from django.contrib import admin
from linkedin import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^temp/$', views.temp),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^discussions/$', views.discussions, name='discussions'),
    url(r'^news/$', views.news, name='news'),
    url('', include('social.apps.django_app.urls', namespace='social')),
)

