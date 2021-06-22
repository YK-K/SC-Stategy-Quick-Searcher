from django.shortcuts import render
from django.utils import timezone
from .models import Strategy
from django.shortcuts import render, get_object_or_404
from .forms import StrategyForm
from django.shortcuts import redirect

# Create your views here.
def index(request):
	return render(request, 'app/index.html', {})
	
def strategy_search(request):
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
		form = StrategyForm
		
	return render(request, 'app/strategy_new.html', {'form': form})
