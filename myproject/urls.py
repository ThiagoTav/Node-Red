# No arquivo urls.py do seu projeto Django (myproject)
from django.urls import path
from myproject.views import receber_dados

urlpatterns = [
    path('dados/', receber_dados, name='receber_dados'),
]