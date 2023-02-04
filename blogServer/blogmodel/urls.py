from django.urls import path
from users.views import UserRegistratiionView
from users.views import UserLoginView
from users.views import UserProfileView
from blogmodel.views import getAllBlogViews
from blogmodel.views import PostListAPIView
from blogmodel.views import getSingleBlogView
from blogmodel.views import updageSingleBlogView
from blogmodel.views import deleteSingleBlogView


from django.urls import path, include
urlpatterns = [
    path('getllblog/', getAllBlogViews.as_view(), 
    name='getallblog'),
    path('postBlog/', PostListAPIView.as_view(), 
    name='getallblog'),
    path('getSingleBlog/', getSingleBlogView.as_view(), 
    name='getSingleBlog'),
    path('updateBlog/', updageSingleBlogView.as_view(), 
    name='updateBlog'),
    path('deleteBlog/', deleteSingleBlogView.as_view(), 
    name='deleteBlog'),
]