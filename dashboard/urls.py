from . import views
from django.urls import include, path


urlpatterns = [
   
    path('', views.plot_metrics_vara_view, name='plot_metrics_vara'),
]