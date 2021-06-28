from django.urls import path
import marioGolf.views as views

urlpatterns = [
    path('', views.base_views.Dashboard.as_view(), name='marioGolfHome'),
    path('characters/', views.base_views.CharacterList.as_view(), name='characterListViewMario'),
    path('characters/<int:pk>/', views.base_views.CharacterDetailView.as_view(), name='detailCharacterMario'),
    path('players/<int:pk>/', views.base_views.PlayerDetailView.as_view(), name='detailPlayerMario'),
    path('tournaments/', views.base_views.TournamentListView.as_view(), name='tournamentListViewMario'),
    path('tournaments/<int:pk>/', views.base_views.TournamentDetailView.as_view(), name='detailTournamentMario'),
    path('tournaments/<int:pk>/leaderboard', views.base_views.TournamentLeaderboardTable.as_view(), name='tournamentLeaderboardMario'),
    path('powerRankingsTable/', views.base_views.PowerRankingsTable.as_view(), name='powerRankingsTable'),
]
