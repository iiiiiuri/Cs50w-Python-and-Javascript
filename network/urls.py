
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("profile/<str:username>/", views.user_profile, name="profile"),
    path("following/", views.followingPage, name="following"),


    #api
    path("create_post/", views.create_post, name="create_post"),
    path("delete_post/<int:id>/", views.delete_post, name="delete_post"),
    path("edit_post/<int:id>/", views.edit_post, name="edit_post"),
    path("do_like/<int:id>/", views.do_like, name="do_like"),
    path("update_profile/<str:username>/", views.update_profile, name="update_profile"),
    path("follow/<int:id>/", views.follow, name="follow"),
]
