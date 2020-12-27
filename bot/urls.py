from django.urls import path
from . import views


urlpatterns = [
    path('', views.BotIndex.as_view(), name='index'),
    path('api/coronabot', views.BotApiView.as_view(), name='chatterbot'),
]
