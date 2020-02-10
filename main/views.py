from django.shortcuts import render
from .models import Travel
from django.core.paginator import Paginator
from django.views.generic import ListView



def home(request):
    p = Paginator(Travel.objects.all().order_by('added'), 18)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    return render(request, 'main/index.html', {'page_obj': page_obj})
