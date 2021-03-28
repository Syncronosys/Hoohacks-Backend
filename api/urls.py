from django.urls import path
from . import views

urlpatterns = [
    path('join/', views.api_join),
    path('update/', views.api_update),
    path('session/', views.api_session),
    path('poll/', views.api_poll)
]
