from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:page>/', views.detail, name='detail'),
    path('search/', views.search, name='search'),
    path('add/', views.add, name='add'),
    path('add_r/', views.add_r, name='add_r'),
    path('detail/<int:pk_num>', views.detail, name='detail'),
]