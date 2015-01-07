from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView, TemplateView
from signup.forms import SignupForm


class MainView(FormView):
    template_name = 'signup/main.html'
    form_class = SignupForm
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        form.save()
        return super(MainView, self).form_valid(form)


class SuccessView(TemplateView):
    template_name = 'signup/success.html'
