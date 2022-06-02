from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import User, Employee, Employer
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import EmployeeSignUpForm, EmployerSignUpForm


def register(request):
    return render(request, '../templates/register.html')


class employee_register(CreateView):
    model = User
    form_class = EmployeeSignUpForm
    template_name = '../templates/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


class employer_register(CreateView):
    model = User
    form_class = EmployerSignUpForm
    template_name = '../templates/employer_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, '../templates/login.html',
                  context={'form': AuthenticationForm()})


def logout_view(request):
    logout(request)
    return redirect('/')


@login_required
def profile(request):
    if request.user.is_employee:
        return render(request, 'employee_profile.html')
    elif request.user.is_employer:
        return render(request, 'employer_profile.html')
