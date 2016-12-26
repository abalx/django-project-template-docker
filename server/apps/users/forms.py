# coding: utf-8

from django import forms
from django.contrib.auth import forms as auth_forms

from apps.users import models


class UserChangeForm(auth_forms.UserChangeForm):
    pass


class UserCreationForm(auth_forms.UserCreationForm):
    pass