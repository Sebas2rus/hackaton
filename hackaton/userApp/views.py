from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.


class Registro(View):

    def get(self, request):
       form= UserCreationForm()
       return render(request, "registro.html",{'form':form})    
     
    def post(self, request):
        form= UserCreationForm(request.POST)
        
        if form.is_valid():
            usuario=form.save()
            login(request,usuario)
            return redirect('index')
        else :
            for msg in form.error_messages:
                   messages.error(request, form.error_messages, msg)
                   return render(request, 'login.html',{'form': form})  
               

def cerrar_sesion(request):
    logout(request)
    return redirect('index')

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password')
            user = authenticate(username=nombre_usuario, password=password1)
            if user is not None:
                login(request, user)
                return redirect('index')
            else: messages.error(request, 'Invalid username or password')
        else: messages.error(request, 'Invalid username or password')
    
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})    