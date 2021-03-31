from django.urls import path

from . import views

urlpatterns = [
    path('', views.Dashboard.as_view(), name='tenMansHome'),
    path('overallWinrateChart/', views.overallWinrateBarChart, name='overallWinrateChart'),
    path('overallWinrateTable/', views.overallWinrateTable, name='overallWinrateTable'),
    path('overallPlaytimeChart/', views.overallPlaytimeBarChart, name='overallPlaytimeChart'),
    path('overallPlaytimeTable/', views.overallPlaytimeTable, name='overallPlaytimeTable')
]