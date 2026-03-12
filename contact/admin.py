from django.contrib import admin
from contact import models

# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone') #mostrar esses campos na listagem
    ordering = ('id',) #ordenar por id
    search_fields = ('id', 'first_name', 'last_name',) #permitir busca por id, first_name e last_name
    list_per_page = 10 #mostrar 10 contatos por página
    list_max_show_all = 100 #limitar a quantidade máxima de contatos que podem ser mostrados na listagem
    list_editable = ('first_name', 'last_name',) #permitir edição direta dos campos first_name e last_name na listagem
    list_display_links = ('id', 'email', 'phone',) #permitir que os campos id, email e phone sejam clicáveis para acessar a página de detalhes do contato

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('id',)
