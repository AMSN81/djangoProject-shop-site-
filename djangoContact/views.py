from django.shortcuts import render
from .forms import contactForm

# Create your views here.
from .models import Contact_us


def contact_page(request):
    form=contactForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        subject = form.cleaned_data.get('subject')
        text = form.cleaned_data.get('text')
        Contact_us.objects.create(name=name, email=email, subject=subject, text=text)
        form = contactForm()
    context={
        'contact_form' : form
    }
    return render(request,"contact_us_page.html",context)