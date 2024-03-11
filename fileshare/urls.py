from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .api_views import UserListCreateAPIView, PostListCreateAPIView
from . import views
from .api_views import UserListCreateAPIView, PostListCreateAPIView



urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('<str:user_name>/upload_file', views.UploadView.as_view(), name='upload_file'),
    path('profile/<str:user_name>', views.ProfileView.as_view(), name='profile'),
    path('delete/<int:post_id>', views.DeleteView.as_view(), name='delete'),
    path('search/', views.SearchView.as_view(), name='search'),
    
    path('api/token/', obtain_auth_token, name='api-token'),
    path('api/users/', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('api/posts/', PostListCreateAPIView.as_view(), name='post-list-create'),
]