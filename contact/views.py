from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from contact.forms import ContactFormModel


# Create your views here.
# def contacts(request: HttpRequest) -> HttpResponse:
#     return render(request, 'contact/information.html')

def submitted_request(request: HttpRequest) -> HttpResponse:
    return render(request, 'contact/thanks.html')

def contacts(request: HttpRequest) -> HttpResponse:
    form = ContactFormModel(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('contact:submitted-request')

    context = {
        'form': form,
    }

    return render(request, 'contact/information.html', context)