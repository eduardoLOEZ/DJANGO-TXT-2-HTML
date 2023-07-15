from django.urls import path
from .views import index

urlpatterns = [
    path('converter/', index, name='index'),
]