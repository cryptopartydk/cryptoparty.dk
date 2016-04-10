from django.conf.urls import url

from .views import (
    PartyCreate, PartyUpdate, PartyList, PartyDetail
)

urlpatterns = [
    url(r'create$', PartyCreate.as_view(), name='party-create'),
    url(r'(?P<slug>\S+)/edit$', PartyUpdate.as_view(), name='party-edit'),
    url(r'(?P<slug>\S+)$', PartyDetail.as_view(), name='party-detail'),
    url(r'$', PartyList.as_view(), name='party-list'),
]
