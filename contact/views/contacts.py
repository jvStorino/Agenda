from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.db.models import Q
from django.core.paginator import Paginator


def index(request):

    contacts = Contact.objects.filter(show=True).order_by("first_name")
    paginator = Paginator(contacts, 10)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
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

    paginator = Paginator(contacts, 10)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
    }

    return render(request, "contact/index.html", context)


def single_contact(request, contact_id):

    contact = get_object_or_404(Contact, id=contact_id)
    context = {
        "contact": contact,
    }

    return render(request, "contact/single_contact.html", context)
