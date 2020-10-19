from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Pet


def index(request):
    pets= Pet.objects.all()
    context = {
        'pets': pets,
    }
   
    return render(request, 'track/index.html', context)

def detail(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)
   
    context = {
        'pet': pet,
    }

    return render(request, 'track/detail.html', context)   
