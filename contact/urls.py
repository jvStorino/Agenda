from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),

    # CRUD contact
    path('contact/<int:contact_id>/', views.single_contact, name='single_contact'),
    path('contact/<int:contact_id>/update/', views.update_contact, name='update_contact'),
    path('contact/create/', views.create_contact, name='create_contact'),
]