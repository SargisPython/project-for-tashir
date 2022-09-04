from django.shortcuts import render
from .models import *
from django.urls import reverse_lazy
from django.db.models import F
from django.views.generic import ListView, FormView, DetailView, CreateView
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView
from .forms import *


class tashir_pizza(ListView):
    model = Tashir_pizza
    template_name = 'index.html'
    context_object_name = 'tashirs'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['socials'] = Social.objects.all()
        context['pizzas'] = Pizza.objects.all()
        context['salats'] = Salat.objects.all()
        context['souss'] = Sous.objects.all()
        context['xohanocys'] = Xohanocy.objects.all()
        context['patmutyuns'] = Patmutyun.objects.all()
        context['jamers'] = Jamer.objects.all()
        context['contacts'] = Contact.objects.all()
        return context


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "register.html", {"form": form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')


class ContactListView(ListView):
    model = Contact
    template_name = 'index.html'
    context_object_name = 'contacts'



class Add_ContactView(CreateView):
    form_class = UserAdd_contactForm
    template_name = 'index.html'
    success_url = reverse_lazy('home')
    raise_exception = True


def add_contact(request):
    if request.method == 'POST':
        form = UserAdd_contactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = UserAdd_contactForm()
    return render(request, ' index.html', {'form': form})

# class ContactListView(ListView):
#     model = Contact
#     template_name = 'index.html'
#     context_object_name = 'contacts'
#
#     def contact(self, request):
#
#         if request.method == 'POST':
#             form = ContactForm(request.post)
#             form.contact = self.contact
#             form.save()
#             return redirect('home')
#         else:
#             form = ContactForm(request.post)
#
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['socials'] = Social.objects.all()
#         context['pizzas'] = Pizza.objects.all()
#         context['salats'] = Salat.objects.all()
#         context['souss'] = Sous.objects.all()
#         context['xohanocys'] = Xohanocy.objects.all()
#         context['patmutyuns'] = Patmutyun.objects.all()
#         context['jamers'] = Jamer.objects.all()
#         context['contacts'] = Contact.objects.all()
#         return context
