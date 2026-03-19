from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.db.models import Q


def index(request):

    contacts = Contact.objects.filter(show=True)[:10]
    context = {
        "contacts": contacts,
    }

    return render(request, "contact/index.html", context)


def search(request):
    search_value = request.GET.get("q", "").strip()

    if search_value == "":
        return redirect("contact:index")

    contacts = (
        Contact.objects.filter(show=True)
        .filter(
            Q(first_name__icontains=search_value)
            | Q(last_name__icontains=search_value)
            | Q(email__icontains=search_value)
            | Q(phone__icontains=search_value)
        )
    )

    context = {
        "contacts": contacts,
    }

    return render(request, "contact/index.html", context)


def single_contact(request, contact_id):

    contact = get_object_or_404(Contact, id=contact_id)
    context = {
        "contacts": contact,
    }

    return render(request, "contact/single_contact.html", context)
