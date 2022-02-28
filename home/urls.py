from django.urls import path
from .views import home,teacher,about


urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("teacher/", teacher, name="teacher"),
]
