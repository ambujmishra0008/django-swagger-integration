from django.urls import path
from . import views

urlpatterns = [
    path('post_member', views.post_member, name='post_member')
]
