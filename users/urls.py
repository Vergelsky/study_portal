from django.urls import path

from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserRetrieveAPIView, UserListAPIView, UserUpdateAPIView, UserDestroyAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('create/', UserCreateAPIView.as_view(), name='user-create'),
    path('', UserListAPIView.as_view(), name='user-list'),
    path('<int:pk>', UserRetrieveAPIView.as_view(), name='user-get '),
    path('update/<int:pk>', UserUpdateAPIView.as_view(), name='user-update'),
    path('delete/<int:pk>', UserDestroyAPIView.as_view(), name='user-delete'),
]
