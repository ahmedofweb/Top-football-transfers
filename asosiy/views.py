from django.shortcuts import render
import datetime
from .models import *

def index(request):
    return render(request, 'index.html')

def clubs(request):
    content = {
        'clubs': Club.objects.all()
    }
    return render(request, 'clubs.html', content)

def players(request):
    content = {
        'players': Player.objects.all().order_by('-cost')
    }
    return render(request, 'players.html', content)

def tryouts(request):
    return render(request, 'tryouts.html')

def u20_players(request):
    h_sana = datetime.datetime.today()
    h_sana = str(h_sana)[:10]
    oldingi = h_sana.replace(h_sana[:4], str(int(h_sana[:4])-20))
    content = {
        "players": Player.objects.filter(
            dob__gte=oldingi,
            dob__lte=h_sana
        ).order_by('-cost', 'dob')
    }
    return render(request, 'U-20 players.html', content)
def stats(request):
    return render(request, 'stats.html')

def about(request):
    return render(request, 'about.html')

def transfer_records(request):
    content = {
        'transfers': Transfer.objects.all().order_by('-selling_cost')
    }
    return render(request, 'transfer-records.html', content)

def transfer_archive(request):
    natija = []
    transfers = Transfer.objects.all().values("season").distinct().order_by("season")
    for i in transfers:
        natija.append(i.get("season"))
    content = {
        "seasons": natija
    }
    return render(request, 'transfer-archive.html', content)

def season_transfers(request, season):
    content = {
        'transfers': Transfer.objects.filter(season=season).order_by('-selling_cost')
    }
    return render(request, '2017-18season.html', content)

def latest_transfers(request):
    present = PresentSeason.objects.last().p_season
    print(present)
    content = {
        'transfers': Transfer.objects.filter(season=present)
    }
    return render(request, 'latest-transfers.html', content)

def club_players(request, pk):
    content = {
        'players': Player.objects.filter(club__id=pk),
        'club': Club.objects.get(id=pk)
    }
    return render(request, 'country-clubs.html', content)

def country_clubs(request, name):  #clubs/<str:name>/
    content = {
        "clubs": Club.objects.filter(country=name.capitalize())
    }
    return render(request, 'england.html', content)