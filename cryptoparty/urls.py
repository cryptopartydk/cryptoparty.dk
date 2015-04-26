from allauth.account.views import LogoutView
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from parties.models import Party
from people.views import ProfileView


class FrontPageView(TemplateView):
    template_name = 'frontpage.html'

    def get_context_data(self, **kwargs):
        context = super(FrontPageView, self).get_context_data(**kwargs)
        context['upcoming'] = Party.objects.upcoming().public()
        context['past'] = Party.objects.past().public()
        return context


urlpatterns = patterns(
    '',
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
    url(
        r'^$', FrontPageView.as_view()
    ),
)
