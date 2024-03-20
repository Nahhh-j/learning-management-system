from django.urls import path
from .views import UserRegistration, UserList, UserDetails, UserLogin, UserLogout, UserDelete

urlpatterns = [
    path('register/', UserRegistration.as_view(), name='register'),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetails.as_view(), name='user-detail'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('delete/', UserDelete.as_view(), name='delete'),
]