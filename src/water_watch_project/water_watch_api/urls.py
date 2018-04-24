from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from water_watch_api import views
from rest_framework.authtoken import views as authviews

router = DefaultRouter()


urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'station_map/$', views.StationMapView.as_view()),
    url(r'dashboard/$', views.DashboardSensorDataView.as_view(), name='dashboard'),
    url(r'home/$', views.HomePageView.as_view(), name='home'),
    url(r'sensor_data/$', views.SensorDataListCreateView.as_view()),
    url(r'sensor_data/(?P<pk>\w+)$', views.SensorDataRetrieveUpdateDestroyView.as_view()),
    url(r'sensor_type/(?P<pk>\w+)$', views.SensorTypeRetrieveUpdateDestroyView.as_view()),
    url(r'sensor_type/$', views.SensorTypeListCreateView.as_view()),
    url(r'sensor_maintenance_history/(?P<pk>\w+)$', views.SensorMaintenanceHistoryRetrieveUpdateDestroyView.as_view()),
    url(r'sensor_maintenance_history/$', views.SensorMaintenanceHistoryListCreateView.as_view()),
    url('signup/', views.SignUpView.as_view(), name='signup'),
    url('signin/', views.SignInView.as_view(), name='signin'),
    url(r'^api-token-auth/', authviews.obtain_auth_token),

    url(r'sensor/update/(?P<pk>\w+)$', views.SensorRetrieveUpdateDestroyView.as_view()),
    url(r'sensor/create/$', views.SensorListCreateView.as_view()),
    url(r'sensor/search/$', views.SensorSearchView.as_view()),
    url(r'sensor/$', views.SensorSearchView.as_view()),

    url(r'station/update/(?P<pk>\w+)$', views.StationRetrieveUpdateDestroyView.as_view()),
    url(r'station/create/$', views.StationListCreateView.as_view()),
    url(r'station/search/$', views.StationSearchView.as_view()),
    url(r'station/$', views.StationSearchView.as_view()),

    url(r'projectdetail/', views.ProjectDetailView.as_view(), name='projectdetail'),
    url(r'aboutus/', views.AboutUsView.as_view(), name='aboutus'),
    url(r'contact/', views.ContactView.as_view(), name='contact'),

]
