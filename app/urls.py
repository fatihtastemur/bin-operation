from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('collection-frequency/', views.collection_frequency, name='collection_frequency'),
]