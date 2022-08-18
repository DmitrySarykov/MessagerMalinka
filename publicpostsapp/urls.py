from django.contrib import admin
from django.urls import path
from publicpostsapp.views import *

urlpatterns = [
    path('', ChatView.as_view(), name='chat'),
    path('messages/',MessagesListAPI.as_view(),name='message_list'),
    path('message/add',MessagesCreateAPI.as_view(),name='message_add'),
]