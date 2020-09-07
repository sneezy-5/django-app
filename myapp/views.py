from django.shortcuts import render, redirect
from .forms import MessageForm

# Create your views here.


def acceuil(request):
    return render(request, 'html/acceuil.html')


def indexx(request):
    return render(request, 'html/quiSomme.html')


def activite(request):
    return render(request, 'html/NosActivite.html')


def contacte(request):
    context ={}
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'html/merci.html', context)

        else:
            context['errors']= form.errors.items()

    else:
        form = MessageForm()
        context['form']= form
 

    return render(request, 'html/indexxxx.html', context)


