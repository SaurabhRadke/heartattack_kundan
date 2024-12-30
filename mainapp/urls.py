from django.urls import path
from . import views

urlpatterns = [
   path('', views.predict_heart_disease, name='predict'),
   path('predictions/', views.prediction_list, name='prediction_list'),
]