from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import forms

# Create your views here.
def logout(request):
    logout(request)

def register(request):
    if request.method == 'POST':
        formulario_post = forms.CustomCreationForm(request.POST)
        if formulario_post.is_valid():
            user = formulario_post.save()
       
            login(request, user)
            return redirect('home')

        else:
            return render(request, 'registration/register.html', {
                'form': forms.CustomCreationForm(),
                'errors' : formulario_post.errors
            })
    return render(request, 'registration/register.html', {
        'form' : forms.CustomCreationForm()
    })