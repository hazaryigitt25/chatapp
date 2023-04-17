from django.db import models

# Create your models here.

class Chat(models.Model):
    chat_name = models.CharField(max_length=15,verbose_name="Chat Name")
    chat_admin = models.CharField(max_length=15,verbose_name="Chat Admin")
    chat_password = models.CharField(max_length=300,verbose_name="Password")
    def __str__(self):
        return self.chat_name
    
class Message(models.Model):
    chat = models.ForeignKey(Chat, verbose_name=("Chat"), on_delete=models.CASCADE,related_name="messages")
    author = models.CharField(max_length=50,verbose_name="Author")
    message = models.CharField(max_length=1500,verbose_name="Message")
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.message
    class Meta:
        ordering = ['created_date'] 