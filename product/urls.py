from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductList.as_view()),
    path('category/<str:slug>/', views.categories_page),
]