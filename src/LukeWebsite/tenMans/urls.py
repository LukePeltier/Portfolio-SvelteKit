from django.urls import path

from . import views

urlpatterns = [
    path('', views.Dashboard.as_view(), name='tenMansHome'),
    path('overallWinrateChart/', views.overallWinrateBarChart, name='overallWinrateChart'),
    path('overallWinrateTable/', views.overallWinrateTable, name='overallWinrateTable'),
    path('overallPlaytimeChart/', views.overallPlaytimeBarChart, name='overallPlaytimeChart'),
    path('overallPlaytimeTable/', views.overallPlaytimeTable, name='overallPlaytimeTable'),
    path('player/<int:pk>/', views.PlayerDetailView.as_view(), name='detailPlayer'),
    path('player/<int:pk>/winrateOTData/', views.PlayerWinrateOverTimeView.as_view(), name='playerWinrateOverTime'),
    path('newgame/', views.NewGameView.as_view(), name='newGameFormView'),
    path('updategame/', views.UpdateGameView.as_view(), name='updateGameFormView'),
    path('updateallgames/', views.UpdateAllGamesView.as_view(), name='updateAllGamesFormView'),
    path('playerDraftStats/', views.PlayerDraftStats.as_view(), name='playerDraftStatsView'),
    path('averagePlayerDraftOrderTable/', views.AverageDraftOrderTable.as_view(), name='averageDraftOrderTable'),
    path('expectedPlayerDraftOrderWinrateTable/', views.ExpectedDraftOrderWinrateTable.as_view(), name='expectedDraftOrderWinrateTable'),
    path('expectedPlayerDraftOrderWinrateTable/<str:lane>', views.ExpectedDraftOrderWinrateLaneTable.as_view(), name='expectedDraftOrderWinrateLaneTable'),
    path('player/<int:pk>/laneCountData/', views.PlayerLaneCountTable.as_view(), name='playerLaneCountTable'),
    path('player/<int:pk>/championCountData/', views.PlayerChampionCountTable.as_view(), name='playerChampionCountTable'),
    path('player/<int:pk>/gamesPlayedData/', views.PlayerGamesTable.as_view(), name='playerGamesTable'),
    path('game/', views.GameListView.as_view(), name='gameListView'),
    path('game/<int:pk>/', views.GameDetailView.as_view(), name='detailGame'),
    path('game/<int:pk>/blueTeamTable/', views.BlueTeamTable.as_view(), name='blueTeamTable'),
    path('game/<int:pk>/redTeamTable/', views.RedTeamTable.as_view(), name='redTeamTable'),
    path('champion/', views.ChampionListView.as_view(), name='championListView'),
    path('champion/<int:pk>/', views.ChampionDetailView.as_view(), name='detailChampion'),
    path('champion/<int:pk>/playtimeChart', views.ChampionPlaytimeChartView.as_view(), name='championPlaytimeChart')
]