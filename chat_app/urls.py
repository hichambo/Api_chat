from django.urls import path

from .views import (
    UserRegistrationView,
    UserRetrieveView,
    UserUpdateView,
    UserDeleteView,
    ChatRoomCreateView,
    ChatRoomRetrieveView,
    ChatRoomUpdateView,
    ChatRoomDeleteView,
    MessageCreateView,
    MessageRetrieveView,
    MessageUpdateView,
    MessageDeleteView,
)

app_name = 'chat'  # Define your app's namespace

urlpatterns = [
    # User endpoints
    path('users/register/', UserRegistrationView.as_view(), name='user-registration'),
    path('users/me/', UserRetrieveView.as_view(), name='user-retrieve'),
    path('users/me/update/', UserUpdateView.as_view(), name='user-update'),
    path('users/me/delete/', UserDeleteView.as_view(), name='user-delete'),

    # Chat room endpoints
    path('chat_rooms/', ChatRoomCreateView.as_view(), name='chatroom-create'),
    path('chat_rooms/<int:pk>/', ChatRoomRetrieveView.as_view(), name='chatroom-retrieve'),
    path('chat_rooms/<int:pk>/update/', ChatRoomUpdateView.as_view(), name='chatroom-update'),
    path('chat_rooms/<int:pk>/delete/', ChatRoomDeleteView.as_view(), name='chatroom-delete'),

    # Message endpoints within chat rooms (using URL nesting)
    path('chat_rooms/<int:chat_room_pk>/messages/', MessageCreateView.as_view(), name='message-create'),
    path('messages/<int:pk>/', MessageRetrieveView.as_view(), name='message-retrieve'),
    path('messages/<int:pk>/update/', MessageUpdateView.as_view(), name='message-update'),
    path('messages/<int:pk>/delete/', MessageDeleteView.as_view(), name='message-delete'),
]
