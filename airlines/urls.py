from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('airline/', views.create_airline, name='create_airline'),
    path('airline/<int:airline_id>/update/',
         views.update_airline, name='update_airline'),
    path('airline/<int:airline_id>/retrieve/',
         views.retrieve_airline, name='retrieve_airline'),
    path('airline/list/', views.list_airlines,
         name='list_airlines'),
    path('aircraft/', views.create_aircraft, name='create_aircraft'),
    path('aircraft/<int:aircraft_id>/update/',
         views.update_aircraft, name='update_aircraft'),
    path('aircraft/<int:aircraft_id>/retrieve/',
         views.retrieve_aircraft, name='retrieve_aircraft'),
    path('aircraft/<int:aircraft_id>/delete/',
         views.delete_aircraft, name='delete_aircraft'),
    path('airline/<int:airline_id>/delete/',
         views.delete_airline, name='delete_airline'),
]
