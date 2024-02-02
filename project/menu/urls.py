from django.urls import path
from . import views

urlpatterns = [
    path('', views.menus, name='menus'),
    path('<int:pk>/', views.menu, name='menu'),
    path('<int:menu_pk>/<slug:path>/', views.categories, name='categories'),
]
