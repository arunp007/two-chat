from django.urls import path
from.import views

urlpatterns = [
    path('home', views.home),
    path('chat1', views.chat1, name ='chat1'),
    path('chat2', views.chat2, name = 'chat2'),
]