from django.conf.urls import url
from .views import *

urlpatterns = [

    url(r'^$', index, name='index'),
    url(r'^display_testery$', display_testery, name='display_testery'),
    url(r'^display_klienci$', display_klienci, name='display_klienci'),
    url(r'^display_DT$', display_DT, name='display_DT'),
    url(r'^display_ph$', display_ph, name='display_ph'),
    url(r'^historia_ph/<phandlowy_id>', historia_ph, name='historia_ph'),

    url(r'^wypozycz_tester/(?P<numer_seryjny>\d+)$', wypozycz_tester, name='wypozycz_tester'),
##    url(r'^dodaj_ph$', dodaj_ph, name='dodaj_ph'),
]
