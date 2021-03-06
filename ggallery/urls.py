from django.contrib import admin
from django.urls import path
from ggallery import views

urlpatterns = [
    path('', views.signin, name='signin'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('student/', views.student, name='student'),
    path('addpin/', views.addpin, name='addpin'),
    path('allpin/', views.allpin, name='allpin'),
    path('pindetails/<int:pk>', views.pindetails, name='pindetails'),
    path('editpin/<int:pk>', views.editpin, name='editpin'),

]
