from django.urls import path
import marioGolf.views as views

urlpatterns = [
    path('', views.base_views.Dashboard.as_view(), name='marioGolfHome')
]
