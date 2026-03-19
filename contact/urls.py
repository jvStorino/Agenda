from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('<int:contact_id>/', views.single_contact, name='single_contact'),
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
]