from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('download-cv/', views.download_cv, name='download_cv'),
]

urlpatterns = [
    path('', views.index, name='index'),
]
