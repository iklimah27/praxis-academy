from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Htampil, name='home'),
    path('Hguru', views.Hguru, name='Hguru'),
    path('Habout', views.Habout, name='Habout'),
    path('sd', views.sd, name='sd'),
    path('smp', views.smp, name='smp'),
    path('<id>/profilgr', views.profilgr),
    path('<no>/form', views.form),
    path('<no>/formklien', views.formklien),
]