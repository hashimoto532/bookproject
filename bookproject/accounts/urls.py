from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from . import views
from .views import SignupView

app_name = 'accounts'

urlpatterns = [
  path('login/',LoginView.as_view(),name='login'),
  path('logout/',views.logout_view,name='logout'),
  path('signup/',SignupView.as_view(),name='signup'),
]