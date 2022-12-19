from django.urls import path
from . import views

urlpatterns = [
    path('add', views.dummy, name='add-dummy'),
    path('add/<int:count>', views.dummydata, name='add-dummy-count'),
]
