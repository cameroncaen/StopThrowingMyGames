from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
    path('find', index),
    path('matchup/<str:matchCode>', index)
]