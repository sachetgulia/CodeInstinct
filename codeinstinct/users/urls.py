from django.urls import path
from users.views.view import UserListView

urlpatterns = [
    path('list/', UserListView.as_view(), name='user-list'),
    # Other URL patterns for your project
]