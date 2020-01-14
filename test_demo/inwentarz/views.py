from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from simple_history.models import HistoricalRecords


def index(request):
    return render(request, 'index.html')


def display_testery(request):
    items = Tester.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'testery.html', context)


def display_klienci(request):
    items = Firma.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'klienci.html', context)


def display_DT(request):
    items = DHandlowiec.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'DT.html', context)


def display_ph(request):
    filter = request.GET.get('nazwa', False)
    items = Phandlowy.objects.filter(firma=filter)
    context = {
        'items': items,
    }
    return render(request, 'ph.html', context)


def wypozycz_tester(request, numer_seryjny):
    item = get_object_or_404(Tester, numer_seryjny=numer_seryjny)
    numer = item.numer_seryjny

    if request.method == "POST":
        form = testerForm(request.POST, instance = item)
        item.wypozyczony = True
        form.save()
        return redirect('display_testery')

    else:
        form = testerForm(instance=item)
        return render(request, 'wypozycz.html', {'form': form, 'numer':numer})


def historia_ph(request):
    filter = request.GET.get('phandlowy_id', False)
    items = Tester.history.filter(phandlowy_id=filter)
    context = {
        'items': items,
    }
    return render(request, 'phandlowy.html', context)


def dodaj_ph(request):
    if request.method == "POST":
        form = nowyPhForm(request.POST)
        form.save()
        return redirect('display_testery')

    else:
        form = nowyPhForm()
        return render(request, 'wypozycz.html', {'form': form})
