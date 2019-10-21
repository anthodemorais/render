from django.urls import path, include
from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/profile/', views.home, name='profile'),
    # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
]