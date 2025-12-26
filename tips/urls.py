# tips/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.tips_list, name='tips_list'),           # /tips/ → list of all tips
    path('<int:tip_id>/', views.tip_detail, name='tip_detail'),  # /tips/1/ → detail of a tip
    path('home/', views.tips_home, name='tips_home'),     # optional generic tips page
]
