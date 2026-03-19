from django.shortcuts import render, get_object_or_404
from contact.models import Contact


def index(request):

    contacts = Contact.objects.filter(show=True)[:10]
    context = {
        'contacts': contacts,
    }
    
    return render(request, 'contact/index.html', context)

def single_contact(request, contact_id):

    contact = get_object_or_404(Contact, id=contact_id)
    context = {
        'contacts': contact,
    }
    
    return render(request, 'contact/single_contact.html', context)