from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='home'),  # Home page or index view
    
    # Menu API endpoints
    path('menu/', views.MenuItemsView.as_view(), name='menu-list'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='menu-detail'),
    
    # Booking API endpoints
    path('bookings/', views.BookingViewSet.as_view({
        'get': 'list',  # GET method for listing all bookings
        'post': 'create'  # POST method to create a new booking
    }), name='booking-list'),
    path('bookings/<int:pk>', views.BookingViewSet.as_view({
        'get': 'retrieve',  # GET method for retrieving a booking by ID
        'put': 'update',  # PUT method for updating a booking by ID
        'delete': 'destroy'  # DELETE method to remove a booking by ID
    }), name='booking-detail'),

    # Token authentication endpoint
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
