from django.shortcuts import render
from .models import Travel
# Create your views here.

def home(request):
    context = {
        'travels' : Travel.objects.all().order_by('-added'),
    }
    return render(request, 'main/index.html', context)