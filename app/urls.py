from django.urls import path
from app.views import get_evaluation

urlpatterns = [path("evaluate/", get_evaluation)]
