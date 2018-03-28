from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from water_watch_api import views

router = DefaultRouter()
router.register(r'sensor_data', views.SensorDataViewSet)

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^', include(router.urls))
]

