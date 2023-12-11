from django.shortcuts import redirect, render
from django.views.generic import FormView, View
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout


class LoginFormView(FormView):
    form_class = LoginForm
    template_name = 'authentication/index.html'


class Login(View):

    def post(self, request):
        data = request.POST
        user = authenticate(request, username=data.get('username'), password=data.get('password'))

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, template_name = 'authentication/index.html', context={"form": LoginForm()})


def logoutBtn(request):
    logout(request)
    return redirect("/")