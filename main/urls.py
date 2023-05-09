from django.urls import path
from . import views
urlpatterns = [
    path('masjid/<int:id>/', views.masjid, name='masjid_url'),
    path('about/<int:id>/', views.about, name='about_url'),
    path('sh_t/<int:id>/', views.sh_t_detail, name='sh_t_url'),
    path('viloyat_detail/<int:id>/', views.viloyat_detail, name='viloyat_detail_url'),
    path('', views.mp, name='mp_url'),
]
