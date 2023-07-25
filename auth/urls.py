from django.urls import path

# from . import views
# from .views import webLoginView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # path('register', views.register, name="register"),
    # path('register-success', views.regsuccess, name="regsuccess"),
    # path('login/', LoginView.as_view(template_name="login.html"), name='login'),
    # path('logout/', LogoutView.as_view(next_page="login"),name="logout"),
    # path('login-success', views.loginsuccess, name="logsuccess"),
]

# path('login/', customLoginView.as_view(), name='login'),