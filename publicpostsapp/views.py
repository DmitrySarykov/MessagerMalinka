from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from rest_framework import status, generics
from .models import Message
from .serializers import *
from django.contrib.auth.mixins import LoginRequiredMixin

class ChatView(LoginRequiredMixin, TemplateView):
    template_name = 'websocket.html'

# Получение всех уведомлений
class MessagesListAPI(generics.ListAPIView):
    serializer_class = MessageSerializer
    
    def get_queryset(self):
        queryset = Message.objects.all().order_by('date') # Сообщения на текущий день
        return queryset

# Добавление уведомления
class MessagesCreateAPI(generics.CreateAPIView):
    serializer_class = MessageSerializer