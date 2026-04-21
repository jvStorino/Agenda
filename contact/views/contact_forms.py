from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from contact.models import Contact
from contact.forms import ContactForm


def create_contact(request):
    form_action = reverse("contact:create_contact")

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            contact = form.save()
            return redirect("contact:update_contact", contact_id=contact.pk)
        
        context = {
            'form': form,
            'form_action': form_action
        }

        return render(request, "contact/create.html", context)

    context = {
        'form': ContactForm(),
        'form_action': form_action
    }

    return render(request, "contact/create.html", context)

def update_contact(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show = True)
    form_action = reverse("contact:update_contact", args=(contact_id,))

    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)

        if form.is_valid():
            contact = form.save()
            return redirect("contact:update_contact", contact_id=contact.pk)
        
        context = {
            'form': form,
            'form_action': form_action
        }

        return render(request, "contact/create.html", context)

    context = {
        'form': ContactForm(instance=contact),
        'form_action': form_action
    }

    return render(request, "contact/create.html", context)