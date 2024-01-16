from django.urls import path
from .views import MatchView

urlpatterns = [
    # for route /home, generate the view MatchView as 
    path('match', MatchView.as_view())
]