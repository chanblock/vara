import json
from django.http import JsonResponse
from django.shortcuts import render
from utils.vara import plots_vara, get_last_three_blocks




def plot_metrics_vara_view(request):
    plot = plots_vara()
    values_last_blocks = get_last_three_blocks()
    
    return render(request, 'dashboard/metrics.html', context={'plot': plot['plot'], 'plot2': plot['plot2'], 'values_last_blocks': values_last_blocks})