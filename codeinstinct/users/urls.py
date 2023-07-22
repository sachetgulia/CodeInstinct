from django.urls import path
import users.views.main as views

app_name = "users"
urlpatterns = [
    path("list/", views.UserListView.as_view(), name="user-list"),
]
