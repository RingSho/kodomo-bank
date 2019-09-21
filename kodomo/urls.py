from django.urls import path

from . import views


app_name = "kodomo"
urlpatterns = [
    path("", views.HomeTemplateView.as_view(), name="home"),
]
