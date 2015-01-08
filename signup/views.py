from django.views.generic import FormView
from signup.forms import SignupForm


class MainView(FormView):
    template_name = 'signup/main.html'
    form_class = SignupForm

    def form_valid(self, form):
        form.save()
        context = self.get_context_data()
        context['success'] = True
        return self.render_to_response(context)

