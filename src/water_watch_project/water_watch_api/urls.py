from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from water_watch_api import views
from rest_framework.authtoken import views as authviews

router = DefaultRouter()


urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'sensor_data/$', views.SensorDataListCreateView.as_view()),
    url(r'sensor_data/(?P<pk>\w+)$', views.SensorDataRetrieveUpdateDestroyView.as_view()),
    url(r'sensor_type/(?P<pk>\w+)$', views.SensorTypeRetrieveUpdateDestroyView.as_view()),
    url(r'sensor_type/$', views.SensorTypeListCreateView.as_view()),
    url(r'sensor_maintenance_history/(?P<pk>\w+)$', views.SensorMaintenanceHistoryRetrieveUpdateDestroyView.as_view()),
    url(r'sensor_maintenance_history/$', views.SensorMaintenanceHistoryListCreateView.as_view()),
    url('signup/', views.SignUpView.as_view(), name='signup'),
    url(r'^api-token-auth/', authviews.obtain_auth_token),
]
