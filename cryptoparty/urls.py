from django.conf.urls import patterns, include, url
from django.contrib import admin
from signup.views import MainView

urlpatterns = patterns('',
    url(r'^$', MainView.as_view(), name='home'),
    url(r'^parties/', include('parties.urls',
                               namespace='parties',
                               app_name='parties')),
    url(r'^admin/', include(admin.site.urls)),
)
