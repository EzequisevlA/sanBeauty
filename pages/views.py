from django.shortcuts import render, redirect
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Professionals, Customer
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from .forms import CustomerForm, ServiceForm
from django.contrib import messages

# Create your views here.

def ajax_login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False})
    return render(request, "pages/Login.html")
@login_required
def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('add_customer') 
        else:
            print(form.errors)  
    else:
        form = CustomerForm()
    return render(request, 'pages/Dashboard.html', {'form': form})




@login_required
def dashboard(request):
    try:
        professional = Professionals.objects.get(user=request.user)
        customers = Customer.objects.filter(professional=professional)
        context = {'customers': customers, 'error': None}
    except Professionals.DoesNotExist:
        # Caso o usuário não tenha um Professional cadastrado
        context = {'customers': [], 'error': "Usuário não cadastrado."}

    return render(request, "pages/Dashboard.html", context)

@login_required
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'pages/CustomerLists.html',{
        'customers':customers
    })

@login_required
def configuration_menu(request):
    form = ServiceForm()
    return render(request,'pages/Configuration.html',{'form':form})

@login_required
def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)

        if form.is_valid():
            
            form.save()
            messages.success(request, "Serviço cadastrado com sucesso!")
            return redirect('add_customer') 
    
    # Se a requisição não for POST ou o formulário for inválido, renderiza a página do formulário
    else:
        form = ServiceForm()

    return render(request, 'Configuration.html', {'form': form})
            