from django.shortcuts import render
from contact.models import Contact

contacts = Contact.objects.filter(show=True)
context = {
    'contacts': contacts,
}

def index(request):
    return render(request, 'contact/index.html', context)