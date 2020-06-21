from django.contrib.auth import authenticate,login,get_user_model,logout
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.utils.http import is_safe_url
from .forms import Login_form,Register_form

from django.shortcuts import render

# Create your views here.


User = get_user_model()
def register_page(request):
    register_form = Register_form(request.POST or None)
    context={
        'form':register_form,
    }
    if register_form.is_valid():
        form.save()
    return render(request,'auth/register.html', context)