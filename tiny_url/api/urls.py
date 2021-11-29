from django.urls import path
from . import views


urlpatterns = [
    path('create', views.create, name='create'),
    path('s/<tiny_id>', views.redirect_short, name='redirect_short'),
]