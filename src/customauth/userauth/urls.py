from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('sign_up', views.register_view, name='signup'),
    path('logout', views.logout_view, name='logout'),
    path('home', views.home_view, name='home')
]
