"""
URL configuration for airlines_odev project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from airlines import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('airline/', views.create_airline, name='create_airline'),
    path('airline/<int:airline_id>/', views.update_airline, name='update_airline'),
    path('airline/<int:airline_id>/retrieve/',
         views.retrieve_airline, name='retrieve_airline'),
    path('airline/list/', views.list_airlines,
         name='list_airlines'),
    path('aircraft/', views.create_aircraft, name='create_aircraft'),
    path('aircraft/<int:aircraft_id>/',
         views.update_aircraft, name='update_aircraft'),
    path('aircraft/<int:aircraft_id>/retrieve/',
         views.retrieve_aircraft, name='retrieve_aircraft'),
    path('aircraft/<int:aircraft_id>/delete/',
         views.delete_aircraft, name='delete_aircraft'),
    path('airline/<int:airline_id>/delete/',
         views.delete_airline, name='delete_airline'),
]
