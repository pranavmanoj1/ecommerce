from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.Create, name="create"),
    path("active_listings", views.index, name="activelsitings"),
    path("closed", views.closed, name="closed"),
    path("watchlist", views.watch, name="watch"),
    path("categories", views.Categories, name="cat"),
    path("category/<str:category>>", views.displayCategory, name="category"),
    path("<str:listing_id>", views.view, name="view"),
    

]
