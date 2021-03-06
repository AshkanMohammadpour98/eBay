from django.urls import path

from . import views
app_name = 'auctions'
urlpatterns = [
    path("", views.index, name="index"),
    path("list/<slug>/<id>", views.detail_page, name="detail"),
    path("category", views.category_page, name="category"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]
