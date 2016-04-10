from allauth.account.views import LogoutView
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from parties.views import PartyList
from people.views import ProfileView


urlpatterns = [
    url(r'^logout/', LogoutView.as_view(), name='logout'),
    url(r'^accounts/profile/', ProfileView.as_view(), name='profile'),
    url(r'^accounts/', include('allauth.urls')),
    url(
        r'^parties/',
        include(
            'parties.urls',
            namespace='parties',
            app_name='parties'
        )
    ),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', PartyList.as_view(), name='party-list'),
]
