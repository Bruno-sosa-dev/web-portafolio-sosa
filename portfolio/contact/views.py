from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm

# Create your views here.

def contact(request):
    data = {
        'form': ContactForm()
    }
    
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect(reverse('contact')+"?ok")
        else:
            data["form"] = contact_form
            return redirect(reverse('contact')+"?fail")
        
    return render(request, "contact/contact.html", data)

    