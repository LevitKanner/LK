from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('contact', views.contact, name='contact'),
    path('<str:page_name>', views.index, name='index'),
    path('', views.index, {'page_name': ''}, name='home')
]
