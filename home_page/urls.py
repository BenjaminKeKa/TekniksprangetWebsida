from django.urls import path
from . import views


urlpatterns = [
    path("", views.index),
    path("om_oss", views.om_oss),
    path("vart_arbete", views.vart_arbete),
    path("dragskapet", views.dragskapet),
    path("webkamera", views.webkamera),
    path("fusion", views.fusion),
    path("stralningsfysik", views.stralningsfysik),
    path("maskiner", views.maskiner),
    path("intervju", views.intervju),
    path("kontakt", views.kontakt),
    path("website", views.website),
    path("fysiker", views.fysiker),
    path("ingenjörer", views.ingenjörer),
    path("munk", views.munk),
    path("per", views.per)

]
