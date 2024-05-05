from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=128)  # Use a secure password hashing mechanism

    # Additional user profile fields (optional)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True)

    # Timestamps for user creation and last login
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

class ChatRoom(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    participants = models.ManyToManyField(User, related_name='chat_rooms')

    # Timestamps for chat room creation
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    read_status = models.BooleanField(default=False)  # Optional for tracking read messages

    def __str__(self):
        return f"{self.sender.username}: {self.content}"
