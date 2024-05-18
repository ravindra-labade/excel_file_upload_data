from django.urls import path
from .views import ProductImportView, Total_Calculate,ProductUpdateView

urlpatterns = [
    path('prod/', ProductImportView.as_view()),
    path('total/', Total_Calculate.as_view()),
    path('update/<int:pk>/', ProductUpdateView.as_view())
]
