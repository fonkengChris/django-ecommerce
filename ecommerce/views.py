from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, get_user_model

from .forms import ContactForm
from products.models import Product


def home_page(request):
    print(request.session.get("firts_name", "Nothing"))
    allProducts = Product.objects.all()
    context = {
        'title': "Welcome User",
        "content": "This is the home page let us get started",
        "featured_title":"Featured Products",
        "allProducts": allProducts,
        "premium_content": "You are also seeing this content because tou are logged in"
    }
    return render(request, "index.html", context,  {})

def service_page(request):
    return render(request, "service.html", {})


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title":"Contact",
        "content":"Wlecome to contact page.",
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    # request.method = "POST"
    # print(request.POST.get('fullname'))
    # print(request.POST.get('email'))
    # print(request.POST.get('content'))
    return render(request, "allForms/contact/contact.html", context, {})



