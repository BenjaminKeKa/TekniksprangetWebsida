from django.http import HttpResponse
from django.shortcuts import render
from .models import Home, Snabbfakta, Summary_om_oss, Intervju


def index(request):
     homepage = Home.objects.all()
     return render(request, "index.html", {"homepage": homepage})


def om_oss(request):
     s_om_oss = Summary_om_oss.objects.all()
     snabbfaktan = Snabbfakta.objects.all()
     return render(request, "om_oss.html", {"s_om_oss": s_om_oss, "snabbfaktan": snabbfaktan})


def vart_arbete(request):
     return render(request, "vart_arbete.html")


def dragskapet(request):
     return render(request, "dragskapet.html")


def webkamera(request):
     return render(request, "webkamera.html")


def fusion(request):
     return render(request, "fusion.html")


def stralningsfysik(request):
     return render(request, "stralningsfysik.html")


def utrustning(request):
     return render(request, "utrustning.html")


def intervju(request):
     intervjun = Intervju.objects.all()
     return render(request, "intervju.html", {"intervjun": intervjun})


def kontakt(request):
     return render(request, "kontakt.html")
