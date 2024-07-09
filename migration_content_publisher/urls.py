from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_pdf, name='upload_pdf'),  # Define the root URL view
    path('upload/', views.upload_pdf, name='upload_pdf'),  # Example of another path
]
