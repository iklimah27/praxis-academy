# from django.contrib import admin
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.tampil),
#     path('tampilmurid/', views.tampilmurid, name='murid'),
#     path('tampilguru/', views.tampilguru, name='pengajar'),
#     path('detailguru/', views.detailguru, name='gdetail'),
#     path('detailmurid/', views.detailmurid, name='mdetail'),

# ]
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.tampil),
    path('tampilguru', views.tampilguru, name='pengajar'),
    path('<id>/detailguru', views.detailguru, name='gdetail'),
    path('<id>/editguru', views.editguru, name='editguru'),
    path('<id>/deleteguru', views.deleteguru, name='gdelete'),
    path('tampilmurid', views.tampilmurid, name='murid'),
    path('<id>/detailmurid', views.detailmurid, name='mdetail'),
    path('<id_murid>/editmurid', views.editmurid, name='editmurid'),
    path('<id>/deletemurid', views.deletemurid, name='mdelete'),

]