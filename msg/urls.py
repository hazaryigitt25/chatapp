from django.contrib import admin
from django.urls import path
from . import views
app_name = "msg"

urlpatterns = [
    path('chats',views.chats,name="chats"),
    path('createchat',views.createchat,name="createchat"),
    path('chat/join/<int:chat_id>',views.loginchat,name="loginchat"),
    path('chat/<int:chat_id>',views.chat,name="chat"),
    path('chat/delete/<int:chat_id>',views.deletechat,name="deletechat"),
    path('profile/<slug:slug>',views.profile,name="profile"),
    path('allchats',views.allchats,name="allchats"),
]
