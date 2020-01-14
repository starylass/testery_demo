from django.db import models
from simple_history.models import HistoricalRecords



class Firma(models.Model):
    nazwa = models.CharField(max_length=200, primary_key=True)
    ulica = models.CharField(max_length=200)
    miejscowosc = models.CharField(max_length=200)
    kod_pocztowy = models.CharField(max_length=200)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Klienci"


    def __str__(self):
        return self.nazwa


class Phandlowy(models.Model):
    imie = models.CharField(max_length=200)
    nazwisko = models.CharField(max_length=200)
    email = models.EmailField()
    telefon = models.IntegerField()
    firma = models.ForeignKey(Firma, on_delete=models.CASCADE)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Siły sprzdażowe - Klient"


    def __str__(self):
        return self.imie+" "+self.nazwisko


class DHandlowiec(models.Model):
    imie = models.CharField(max_length=200)
    nazwisko = models.CharField(max_length=200)
    email = models.EmailField()
    telefon = models.IntegerField()
    firma = models.ForeignKey(Firma, on_delete=models.CASCADE, default = 'Delphi')
    history = HistoricalRecords()


    class Meta:
        verbose_name_plural = "Siły sprzdażowe - Delphi"


    def __str__(self):
        return self.imie+" "+self.nazwisko


class Tester(models.Model):
    numer_seryjny = models.IntegerField(primary_key=True)
    licencja_car = models.BooleanField(default=True)
    licencja_hd = models.BooleanField(default=True)
    dhandlowiec = models.ForeignKey(DHandlowiec, null=True, on_delete=models.SET_NULL)
    phandlowy = models.ForeignKey(Phandlowy, null=True, on_delete=models.SET_NULL, blank=True)
    wypozyczony = models.BooleanField(default=True)
    data_wypozyczenia = models.DateField(blank=True, null=True)
    problemy = models.CharField(max_length=2000, default="Brak problemów")
    history = HistoricalRecords()


    class Meta:
        verbose_name_plural = "Testery diagnostyczne"


    def __str__(self):
        return '{} - Właściciel: {} - Wypożczony: {}'.format(self.numer_seryjny, self.dhandlowiec, self.wypozyczony)
