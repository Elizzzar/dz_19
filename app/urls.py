from django.urls import path
from .views import  Sign_Up, Log_out, Login, UserCreateView, UserListView, UserDetailView
urlpatterns = [
    path('', UserListView, name = 'user_list'),
    path('user_create/', UserCreateView, name = 'user_create'),
    path('user_detail/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('sign_up/', Sign_Up.as_view(), name='sign_up'),
    path('login/', Login.as_view(), name='login'),
    path('log_out/', Log_out.as_view(), name='log_out'),
]