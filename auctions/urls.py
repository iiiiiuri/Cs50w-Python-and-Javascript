from django.urls import path
from .views import serve_image
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_auction", views.create_auction, name="create_auction"),
    path("watchlist", views.watchlist, name="watch"),
    path('show/<int:id>', views.show, name='show'),
    path('removeWatchList/<int:id>/', views.removeWatchList, name='removeWatchList'),
    path('addWatchList/<int:id>/', views.addWatchList, name='addWatchList'),
    path('doBid/<int:id>/' , views.doBide, name='doBid'),
    path('closeAuction/<int:id>/' , views.closeAuction, name='closeAuction'),
    path('user/<int:user_id>/image/', serve_image, name='serve_image'),
    path('comment/<int:id>/', views.comment, name='comment'),
    path('categories', views.categories, name='categories'),

    ]
