from django.urls import path
from .views import ChatAPIView, chat_view

urlpatterns = [
    path('', chat_view, name='chat-interface'),
    path('api/', ChatAPIView.as_view(), name='chat-api'),
]

