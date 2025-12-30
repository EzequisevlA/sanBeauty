from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views 
from .views import add_customer, add_service

urlpatterns=[
    path("", views.ajax_login, name="ajax_login"),
    path("pages/Dashboard/",views.dashboard, name="dashboard"),
    path("logout/", auth_views.LogoutView.as_view(next_page='/'), name="logout"),
    path('add_customer/', add_customer, name='add_customer'),
    path('customers/list/',views.customer_list, name='customer_list' ),
    path('configuration/', views.configuration_menu, name="configuration"),
    path('add_service/', views.add_service, name='add_service')
]