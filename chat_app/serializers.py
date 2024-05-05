from rest_framework import serializers
from .models import User, ChatRoom, Message

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'profile_picture')

class ChatRoomSerializer(serializers.ModelSerializer):
    participants = serializers.ManyToManyField(User, related_name='chat_room_participants')

    class Meta:
        model = ChatRoom
        fields = ('id', 'name', 'description', 'owner', 'participants', 'created_at')

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    chat_room = ChatRoomSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ('id', 'sender', 'chat_room', 'content', 'timestamp', 'read_status')
