from django.db.models import QuerySet, Q
from django.utils import timezone


class PartyQuerySet(QuerySet):

    def public(self):
        return self.filter(public=True)

    def upcoming(self):
        now = timezone.now()
        return self.filter(
            Q(start__gt=now) |
            Q(start__lt=now, end__gt=now),
        )

    def past(self):
        now = timezone.now()
        return self.filter(
            (
                Q(end__lt=now) |
                ~Q(start__lt=now, end__gt=now)
            ),
            start__lt=now
        )
