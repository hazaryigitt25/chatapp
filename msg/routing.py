from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/msg/chat/<int:id>/',consumers.ChatConsumer.as_asgi()),
]