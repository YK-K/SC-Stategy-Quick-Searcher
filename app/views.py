from django.shortcuts import render
from django.utils import timezone
from .models import Strategy
from django.shortcuts import render, get_object_or_404
from .forms import StrategyForm
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import Q
from django.views.generic.edit import FormView

# Create your views here.
def index(request):
	return render(request, 'app/index.html', {})
	
def strategy_search(request):
	search_keyword = request.GET.get('q', '')
	search_type = request.GET.get('type', '')
	
	if search_keyword:
		if search_type == 'title':
			strategies = Strategy.objects.filter(Q (title__icontains=search_keyword) | Q (content__icontains=search_keyword)).order_by('created_date')
		elif search_type == 'playerRace':
			strategies = Strategy.objects.filter(Q (playerRace__icontains=search_keyword)).order_by('created_date')
		elif search_type == 'enemyRace':
			strategies = Strategy.objects.filter(Q (enemyRace__icontains=search_keyword)).order_by('created_date')
		elif search_type == 'keyUnit':
			strategies = Strategy.objects.filter(Q (keyUnit__icontains=search_keyword)).order_by('created_date')
		elif search_type == 'strategyType':
			strategies = Strategy.objects.filter(Q (strategyType__icontains=search_keyword)).order_by('created_date')
		elif search_type == 'mapname':
			strategies = Strategy.objects.filter(Q (mapname__icontains=search_keyword)).order_by('created_date')

	else:
		strategies = Strategy.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
	
	return render(request, 'app/search.html', {'strategies': strategies})
	
def strategy_detail(request, pk):
	strategy = get_object_or_404(Strategy, pk=pk)
	return render(request, 'app/strategy_detail.html', {'strategy': strategy})
	
def strategy_new(request):
	if request.method == "POST":
		form = StrategyForm(request.POST)
		if form.is_valid():
			strategy = form.save(commit=False)
			strategy.save()
			return redirect('strategy_detail', pk=strategy.pk)
	else:
		form = StrategyForm
		
	return render(request, 'app/strategy_new.html', {'form': form})
	
def strategy_edit(request, pk):
	strategy = get_object_or_404(Strategy, pk=pk)
	if request.method == "POST":
		form = StrategyForm(request.POST, instance=strategy)
		if form.is_valid():
			strategy = form.save(commit=False)
			strategy.modified_date = timezone.now()
			strategy.save()
			return redirect('strategy_detail', pk=strategy.pk)
	else:
		form = StrategyForm(instance = strategy)
		
	return render(request, 'app/strategy_new.html', {'form': form})
