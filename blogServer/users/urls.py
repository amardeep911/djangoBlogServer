
from django.urls import path
from users.views import UserRegistratiionView
from users.views import UserLoginView
from users.views import UserProfileView
urlpatterns = [
    path('register/', UserRegistratiionView.as_view(), 
    name='register'),
    path('login/', UserLoginView.as_view(), 
    name='login'),
    path('profile/', UserProfileView.as_view(), 
    name='profile'),

]