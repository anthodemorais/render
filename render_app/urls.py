from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ProjectsListView.as_view(), name='home'),
    path('project/<int:pk>', views.ProjectsDetailView.as_view(), name="project_detail"),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/profile/', views.home, name='profile')
]