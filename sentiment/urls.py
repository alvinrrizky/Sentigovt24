from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'sentiment'

urlpatterns = [
    path('scrape', views.scrape, name="index"),
    # sentiment
    path('search', views.ManualSearchView.as_view(), name="manualSearch"),
    path('getTrenTotalSentiment', views.getTrenTotalSentiment, name='getTrenTotalSentiment'),
    path('getTrenTotalTweet/', views.getTrenTotalTweet, name='getTrenTotalTweet'),
    path('getTotalTweet/', views.getTotalTweet, name='getTotalTweet'),
    path('getTweetList', views.getTweetList, name='getTweetList'),
    path('getBacapresRanking', views.getRankingBacapres, name="getRankingBacapres"),
    path('generateCSV', views.generateCSV, name="generateCSV"),
    # history
    path('history', views.HistoryView.as_view(), name="getHistoryList"),
    path('history/<int:id>/detail', views.HistoryDetailView.as_view(), name="getDetailHistory"),
    path('history/<int:id>/delete', views.HistoryView.as_view(), name="deleteHistory"),
    path('history/delete/all/', views.HistoryDeleteAllView.as_view(), name="deleteAllHistory"),
]
        
        