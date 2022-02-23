from django.urls import path
from .views import PlayersAbove90,OverallNational

urlpatterns=[
    path('',PlayersAbove90.as_view()),
    path('overall/',OverallNational.as_view()),
]