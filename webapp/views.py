from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.models import User

from .models import *
from .form import LoginForm
from .forms import MovieModelForm

def Home_Page(request):
    movie_qs = Movie.objects.all()
    user_qs = User.objects.all()
    context = {
        "movie_count":movie_qs.count(),
        "user_count":user_qs.count(),
        "movie_qs": movie_qs[0:3],
    }
    return render(request, 'movie_htmlfiles/home_page.html', context)

def movie_details_page(request,id):
    obj = get_object_or_404(Movie, id=id)
    context = {
        "object":obj,
    }
    return render(request, 'movie_htmlfiles/movie_detail.html', context)

def movie_upload_page(request):
    message = None
    form = None
    if request.method == "POST":

        form = MovieModelForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            message = "Saved successfully."
            id = obj.id
            return redirect("movie_details",id)

        else:
            print(form.errors)
    context = {
    "message":message,
    "form":form,
    }
    return render(request, 'movie_htmlfiles/add_movie.html', context)


def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            cd =form.cleaned_data
            user = authenticate(request,
                                username = cd['username'],
                                password = cd['password'])

            if user is not None:
                login(request,user)
                return HttpResponse('Authentication was successful')
            else:
                return HttpResponse('Authentication failed')
    else:
        form = LoginForm()

    return render(request,'login.html',{'form':form})

#dDjango user regostration, user pofile

from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect,get_object_or_404
from webapp.models import RegistrationData
from webapp.forms import RegistrationForm,LoginForm


def registration_view(request):
    if request.method == "POST":
        rform = RegistrationForm(request.POST)
        if rform.is_valid():
            fname = request.POST.get('first_name')
            lname = request.POST.get('last_name')
            uname = request.POST.get('user_name')
            pwd = request.POST.get('password')
            mobile = request.POST.get('mobile')
            email = request.POST.get('email')
            data = RegistrationData(
                first_name=fname,
                last_name=lname,
                user_name=uname,
                password=pwd,
                mobile=mobile,
                email=email
            )
            data.save()
            rform = RegistrationForm()
            return render(request, 'movie_htmlfiles/reg.html', {'rform': rform})
        else:
            return HttpResponse('USer Invalid Data')
    else:
        rform = RegistrationForm()
        return render(request,'movie_htmlfiles/reg.html',{'rform':rform})

def Login_View(request):
    if request.method =="POST":
        lform = LoginForm(request.POST)
        if lform.is_valid():
            uname = request.POST.get('user_name')
            pwd = request.POST.get('password')

            user = RegistrationData.objects.filter(user_name=uname)
            password = RegistrationData.objects.filter(password=pwd)

            if user and password:
                return redirect('/home_page/')
                # return HttpResponse("Success")
            else:
                return HttpResponse("Fail")
        else:
            return HttpResponse('User Invalid Data')
    else:
        lform = LoginForm()
        return render(request,'movie_htmlfiles/logindata.html',{'lform':lform})


































#---------------------------------------------------------------------------------------------- views for authentication
# class LoginView(SuccessURLAllowedHostsMixin, FormView):
#     template_name = 'registration/login.html'
# class LogoutView(SuccessURLAllowedHostsMixin, TemplateView):
# 	template_name = 'registration/logged_out.html'
# class PasswordResetView(PasswordContextMixin, FormView):
# 	template_name = 'registration/password_reset_form.html'
# class PasswordResetDoneView(PasswordContextMixin, TemplateView):
# 	template_name = 'registration/password_reset_done.html'
# class PasswordResetConfirmView(PasswordContextMixin, FormView):
# 	template_name = 'registration/password_reset_confirm.html'
# class PasswordChangeView(PasswordContextMixin, FormView):
# 	template_name = 'registration/password_change_form.html'
# class PasswordChangeDoneView(PasswordContextMixin, TemplateView):
# 	template_name = 'registration/password_change_done.html'

