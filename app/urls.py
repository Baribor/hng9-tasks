from django.urls import path
from app.views import get_user

urlpatterns = [
    path('getUser/', get_user),
]