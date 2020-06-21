from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views #webapp

urlpatterns = [

    path('accounts/', include('django.contrib.auth.urls')), # django.contrib.auth.urls helps tp accesss all views from login logout password set and reset
    path('home/', TemplateView.as_view(template_name='MyApp/home.html'), name='home'),
    #urls related to login reg etc
    path('reg/', views.registration_view),
    path('', views.Login_View),
    path('home_page/',views.Home_Page,name='home_page'),
    
    path('add/movie/',views.movie_upload_page,name='add_movie'),
    path('movie/details/<int:id>',views.movie_details_page,name='movie_details'),


]




# accounts urls for ref
#
# admin/
# accounts/ login/ [name='login']
# accounts/ logout/ [name='logout']
# accounts/ password_change/ [name='password_change']
# accounts/ password_change/done/ [name='password_change_done']
# accounts/ password_reset/ [name='password_reset']
# accounts/ password_reset/done/ [name='password_reset_done']
# accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/ reset/done/ [name='password_reset_complete']
# [name='home']