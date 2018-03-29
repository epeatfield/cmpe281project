from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from water_watch_api import views

router = DefaultRouter()


urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'sensor_data/$', views.SensorDataListCreateView.as_view()),
    url(r'sensor_type/(?P<pk>\w+)$', views.SensorTypeRetrieveUpdateDestroyView.as_view()),
    url(r'sensor_type/$', views.SensorTypeListCreateView.as_view()),
]


