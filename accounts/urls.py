from django.urls import path
from .views import user_login, user_signup, get_user_list, get_user_detail

urlpatterns = [
    path('login/', user_login, name='user_login'),
    path('signup/', user_signup, name='user_signup'),
    path('users/', get_user_list, name='get_user_list'),
    path('users/<int:user_id>/', get_user_detail, name='get_user_detail'),
    # path('users/<int:user_id>/delete/', delete_user, name='delete_user'),
]