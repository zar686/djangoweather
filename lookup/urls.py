from django.urls import path
# This lets us import views from this urls.py director
from . import views

# add all url pages that are created and where they point to
urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
]
