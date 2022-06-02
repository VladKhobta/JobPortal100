from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import Employer, Employee, User


class EmployerSignUpForm(UserCreationForm):
    designation = forms.CharField(required=True)
    location = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employer = True
        user.save()
        employer = Employer.objects.create(user=user)
        employer.designation = self.cleaned_data.get('designation')
        employer.location = self.cleaned_data.get('location')
        employer.phone_number = self.cleaned_data.get('phone_number')
        employer.save()
        return user


class EmployeeSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    location = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employee = True
        user.save()
        employee = Employee.objects.create(user=user)
        employee.first_name = self.cleaned_data.get('first_name')
        employee.last_name = self.cleaned_data.get('last_name')
        employee.phone_number = self.cleaned_data.get('phone_number')
        employee.location = self.cleaned_data.get('location')
        employee.save()
        return user
