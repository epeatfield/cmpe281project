from django.conf.urls import url
from water_watch_api import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
]