#files.py
from __future__ import unicode_literals

from collections import OrderedDict

from django import forms
from django.template import loader
from django.utils.encoding import force_bytes
from django.utils.html import format_html, format_html_join
from django.utils.http import urlsafe_base64_encode
from django.utils.safestring import mark_safe
from django.utils.text import capfirst
from django.utils.translation import ugettext, ugettext_lazy as _

from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.hashers import UNUSABLE_PASSWORD_PREFIX, identify_hasher
from django.contrib.auth.tokens import default_token_generator


import re
from django import forms
from django.contrib.auth.models import User
#from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class userCreation(UserCreationForm):
  email = forms.EmailField(required = True)
  
  class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2')
     
    def save(self, commit = True):
      #user = super(UserCreationForm, self).save(commit = False)
      #user.email = self.cleaned_data['email']
      user = User.objects.create_user(
      username=form.cleaned_data['username'],
      password=form.cleaned_data['password1'],
      email=form.cleaned_data['email']
      )
      #if commit:
        #user.save()
      return user
