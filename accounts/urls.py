from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView


app_name = 'account'

urlpatterns = [
    # auth
    path('register', views.RegisterView.as_view(), name="register"),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logoutRequest, name="logout"),
    # profile
    path('profile', views.UserProfileView.as_view(), name="profile"),
    path('change-password', views.ChangePasswordView.as_view(), name="changePassword"),
    # user management
    path('account', views.AccountListView.as_view(), name="userManagement"),
    path('account/<int:id>/delete', views.AccountListView.as_view(), name="deleteUser"),
    path('account/<int:id>/edit', views.AccountDetailView.as_view(), name="editUser")
]