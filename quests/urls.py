from unicodedata import name
from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    # path('admin/',admin.site.urls),
    # path("", views.base, name='base'),
    path('home/', views.home, name='home'),
    path('about/',views.about, name='about'),
    path('question/',views.question, name='question'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),

    path('signup/', views.signup, name='signup'),
    path('aa/', views.aa, name='aa'),
    path('js/', views.js, name='js'),
]