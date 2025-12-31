from django.urls import path
from .views import home,register, save_result,games,save_score,leaderboard

urlpatterns = [
    path("", home, name="home"),
     path("register/", register, name="register"),
    path("save-result/", save_result, name="save_result"),
    path('games/', games, name='games'),
    path("save-score/", save_score, name="save_score"),
    path("leaderboard/", leaderboard, name="leaderboard"),
]
