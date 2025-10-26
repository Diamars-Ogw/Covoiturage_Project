from django.urls import path
from .views import (
    CreateUserView, 
    UserListView, 
    UpdateUserView,
    DeleteUserView,
    ChangePasswordView
)

urlpatterns = [
    path('createusers/', CreateUserView.as_view(), name='create-user'),
    path('users/', UserListView.as_view(), name='list-users'),
    path('updateusers/<int:pk>/', UpdateUserView.as_view(), name='update-user'),
    path('deleteusers/<int:pk>/', DeleteUserView.as_view(), name='delete-user'),
    path('users/change_password/', ChangePasswordView.as_view(), name='user-change-password'),
]
