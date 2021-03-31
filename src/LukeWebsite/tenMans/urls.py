from django.urls import path

from . import views

urlpatterns = [
    path('', views.Dashboard.as_view(), name='tenMansHome'),
    path('overallWinrateChart/', views.overallWinrateBarChart, name='overallWinrateChart'),
    path('overallWinrateTable/', views.overallWinrateTable, name='overallWinrateTable'),
    path('overallPlaytimeChart/', views.overallPlaytimeBarChart, name='overallPlaytimeChart'),
    path('overallPlaytimeTable/', views.overallPlaytimeTable, name='overallPlaytimeTable'),
    path('player/<int:pk>/', views.PlayerDetailView.as_view(), name='detailPlayer'),
    path('player/<int:pk>/winrateOTData', views.PlayerWinrateOverTimeView.as_view(), name='playerWinrateOverTime'),
    path('newgame/', views.NewGameView.as_view(), name='newGameFormView')
]