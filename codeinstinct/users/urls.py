from django.urls import path
import users.views.view as views

urlpatterns = [
    path("list/", views.UserListView.as_view(), name="user-list"),
    path(r"^$", views.home, name="home"),
    path(r"^signup$", views.signup, name="signup"),
    path(r"^signup/validate$", views.signup_validate, name="signup_validate"),
    path(r"^login$", views.c_login, name="login"),
    path(r"^login/send_otp$", views.send_otp, name="send_otp"),
    path(r"^login/validate$", views.login_validate, name="login_validate"),
    # path(r'^search$', views.search, name="search"),
    path(r"^logout$", views.c_logout, name="logout"),
]
