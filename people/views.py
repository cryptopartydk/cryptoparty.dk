from django.core.exceptions import PermissionDenied
from django.views.generic import DetailView
from cryptoparty.mixins import LoginRequiredMixin

from .models import Profile


class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'people/profile_detail.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        user = self.request.user
        if user.is_authenticated():
            return self.model.objects.get(user=user)
        else:
            raise PermissionDenied()
