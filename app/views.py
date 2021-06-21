from django.shortcuts import render
from django.utils import timezone
from .models import Strategy

# Create your views here.
def index(request):
	return render(request, 'app/index.html', {})
	
def strategy_search(request):
	strategies = Strategy.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
	return render(request, 'app/search.html', {'strategies':strategies})
