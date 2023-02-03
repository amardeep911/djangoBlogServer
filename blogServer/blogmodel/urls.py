from django.urls import path
from users.views import UserRegistratiionView
from users.views import UserLoginView
from users.views import UserProfileView
from blogmodel.views import getAllBlogViews
from blogmodel.views import PostListAPIView


from django.urls import path, include
urlpatterns = [
    path('getllblog/', getAllBlogViews.as_view(), 
    name='getallblog'),
    path('postBlog/', PostListAPIView.as_view(), 
    name='getallblog'),
]