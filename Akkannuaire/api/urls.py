from django.urls import path

from . import views

urlpatterns = [
    path('test', views.get_bm_cdr_liste, name="api-get-bm-cdr"),
]