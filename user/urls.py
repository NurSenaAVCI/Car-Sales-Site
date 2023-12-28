from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view, name='login_page'),
    path('logout/', logout_view, name='logout_page'),
    path('signup/', signup_view, name='signup_page'),
    path('profile/', profile_view, name='profile_page'),
    path('password/', password_change, name='password_page')
]
