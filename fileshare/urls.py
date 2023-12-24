# fileshare/urls.py
from django.urls import path
# from .views import UserLogin, FileUpload, CSRFProtectedView
from . import views
from .api_views import UserListCreateAPIView, PostListCreateAPIView


# urlpatterns = [
#     path('', UserLogin.as_view(), name='user_login'),
#     path('upload/', FileUpload.as_view(), name='file_upload'),    # path('file_UP/',views.test_func, name='test_func')
#     path('csrf/', CSRFProtectedView.as_view(), name='csrf_protected_view'),
# ]

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('<str:user_name>/upload_file', views.UploadView.as_view(), name='upload_file'),
    path('profile/<str:user_name>', views.ProfileView.as_view(), name='profile'),
    path('delete/<int:post_id>', views.DeleteView.as_view(), name='delete'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('api/users/', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('api/posts/', PostListCreateAPIView.as_view(), name='post-list-create'),
]