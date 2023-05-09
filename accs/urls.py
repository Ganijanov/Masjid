from django.urls import path
from . import views
urlpatterns = [
    path('AdminLog-inSs/', views.loginForAdmin, name='pfa_url' )
]
