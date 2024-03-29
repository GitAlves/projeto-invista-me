"""
URL configuration for site_invista_me project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from invista_me import views

urlpatterns = [
    path('', views.pagina_inicial),
    path('novo_investimento/', views.novo_investimento, name='novo_investimento'),  # noqa: E501;
    path('investimento_registrado/', views.investimento_registrado, name='investimento_registrado')  # noqa: E501;
]
