from django.urls import path
from .views import MatchView, PopulateMatchupInfo, GetMatchInfo

urlpatterns = [
    # for route /home, generate the view MatchView as 
    path('match', MatchView.as_view()),
    path('gen-stats', PopulateMatchupInfo.as_view()),
    path('get-stats', GetMatchInfo.as_view())
]