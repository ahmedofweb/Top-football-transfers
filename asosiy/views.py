from django.shortcuts import render
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
        'players': Player.objects.all()
    }
    return render(request, 'players.html', content)

def tryouts(request):
    return render(request, 'tryouts.html')

def last_transfers(request):
    return render(request, 'latest-transfers.html')

def u_20players(request):
    return render(request, 'U-20 players.html')

def stats(request):
    return render(request, 'stats.html')

def about(request):
    return render(request, 'about.html')
