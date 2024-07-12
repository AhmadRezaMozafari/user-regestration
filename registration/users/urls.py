from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.indexPage,name='index'),
    path('',views.logIn,name='log-in'),
    path('register/',views.register_user,name='register'),
    path('log-out/',views.logOut,name='log-out')
]
