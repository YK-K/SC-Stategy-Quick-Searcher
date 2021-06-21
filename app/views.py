from django.shortcuts import render
from django.utils import timezone
from .models import Strategy
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
	return render(request, 'app/index.html', {})
	
def strategy_search(request):
	strategies = Strategy.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
	return render(request, 'app/search.html', {'strategies': strategies})
	
def strategy_detail(request, pk):
	strategy = get_object_or_404(Strategy, pk=pk)
	return render(request, 'app/strategy_detail.html', {'strategy': strategy})
