from . import views
from django.urls import path, include

urlpatterns = [
    path('sighup/', views.RegisterView.as_view(), name='user-signup'),
]