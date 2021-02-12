from django.urls import path
from authentication.views import LoginView, LogOutView

app_name = 'authentication'
urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogOutView.as_view(), name="logout"),
]
