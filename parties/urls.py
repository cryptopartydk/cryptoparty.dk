from django.conf.urls import patterns, include, url

from .views import PartyCreate, PartyList, PartyDetail, PartyAjaxUpdate

urlpatterns = patterns('',
    url(r'create$', PartyCreate.as_view(), name='party-create'),
    url(r'update/(?P<pk>\d+)$', PartyAjaxUpdate.as_view(), name='party-ajax-update'),
    url(r'(?P<slug>\S+)\?key=(?P<key>.*)$', PartyDetail.as_view(), name='party-detail-with-key'),
    url(r'(?P<slug>\S+)$', PartyDetail.as_view(), name='party-detail'),
    url(r'$', PartyList.as_view(), name='party-list'),
)
