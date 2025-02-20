from django.urls import path
from djangoapp import views

urlpatterns = [
    path("", views.home, name="index"),  # Root URL ("/") loads home.html
    path("history/", views.history, name="History"),
    path("leadership/", views.leadership, name="Leadership"),
    path("sites/", views.sites, name="Sites"),
]
