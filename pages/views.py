from django.shortcuts import render, redirect
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Professionals, Customer
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from .forms import CustomerForm

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
            form.save()  # salva no SQLite
            return redirect('add_customer')  # ou qualquer página de sucesso
        else:
            print(form.errors)  # adiciona isso para ver erros no console
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