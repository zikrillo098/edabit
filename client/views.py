from django.shortcuts import render, redirect
from .models import User
from django.views.generic import ListView, View
from django import http
from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.views import LoginView


class ClientRegistration(View):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.title = _("Royxatdan o'tish")

    def get(self, request):
        return render(request, 'layout/form.html', {
            'form': RegisterForm()
        })

    def post(self, request):
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            messages.success(request, _('Siz Muvafqiyatli otdingiz'))
            return redirect('main:index')
        else:
            form = RegisterForm()
        return render(request, 'layout/form.html', {
            'form': form
        })


class Login(LoginView):
    model = User


