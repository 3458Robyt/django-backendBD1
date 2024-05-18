from django.urls import path
from . import views

urlpatterns = [
    path('api/login/', views.login_view, name='api-login'),
    path('api/register/', views.register_view, name='api-register'),
    path('api/profile/', views.profile_view, name='api-profile')
]
