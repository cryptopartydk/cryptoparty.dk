from django.conf.urls import patterns, include, url
from django.contrib import admin
from signup.views import MainView, SuccessView

urlpatterns = patterns('',
    url(r'^success$', SuccessView.as_view(), name='success'),
    url(r'^$', MainView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
