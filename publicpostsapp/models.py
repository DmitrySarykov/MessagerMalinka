from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Message(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
	username = models.CharField(max_length=50, blank=True, null=True, default="", verbose_name="Имя пользователя")
	date = models.DateTimeField(default=datetime.now, verbose_name='Дата')
	text = models.TextField(null=True, blank=True, verbose_name='Текст')

	def __str__(self):
		return self.text
	
	def save(self, *args, **kwargs):
		self.username = self.user.username
		super(Message, self).save(*args, **kwargs)

	class Meta:
		ordering = ('-date',)
		verbose_name = 'Сообщение'
		verbose_name_plural = 'Сообщения'