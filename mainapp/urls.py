from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns=[
    path("", tashir_pizza.as_view(), name="home"),
    path("register", register, name="register"),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path("contact/", ContactListView.as_view(), name="contact"),
    path("add_contact/", add_contact, name="add_contact"),

]