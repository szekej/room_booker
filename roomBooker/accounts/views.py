from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import UserSignUpForm


# Create your views here.

class SignUp(CreateView):
    form_class = UserSignUpForm
    success_url = reverse_lazy('login')  # Przekierowanie po udanej rejestracji
    template_name = 'accounts/signup.html'
