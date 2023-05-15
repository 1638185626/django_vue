from django.urls import path
from .views import test_api

urlpatterns = [
    path('testapi',test_api),
]