from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('search.html', views.strategy_search, name='strategy_search'),
    path('strategy/<int:pk>/', views.strategy_detail, name='strategy_detail'),
]
