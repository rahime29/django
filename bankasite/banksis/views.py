from django.shortcuts import render
from .models import Musteri
# Create your views here.


def musteri_list(request):
    musteriler = Musteri.objects.all()
    return render(request, 'banksis/musteri_list.html', {'musteriler':musteriler})
