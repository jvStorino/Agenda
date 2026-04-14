from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# id (primary key - automático)
# first_name (string), last_name (string), phone (string)
# email (email), created_date (date), description (text), show (boolean), picture (imagem), category (foreign key)

# Depois
# owner (foreign key)

class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"
        verbose_name = "Category"

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Contact(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Primeiro nome')
    last_name = models.CharField(max_length=50, verbose_name='Sobrenome')
    phone = models.CharField(max_length=20, verbose_name='Telefone')
    email = models.EmailField(max_length=254, verbose_name='E-mail')
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True, verbose_name='Descrição')
    show = models.BooleanField(default=True)
    picture = models.ImageField(upload_to='pictures/%Y/%m', blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Categorias')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
