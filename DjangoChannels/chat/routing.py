from django.urls import path
from . import consumers  # Импортируем наш Consumer

websocket_urlpatterns = [
    path('ws/chat/', consumers.ChatConsumer.as_asgi()),
]
