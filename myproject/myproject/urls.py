from django.contrib import admin
from django.urls import path, include
from myapp.views import AirplaneViewSet, FlightViewSet, TicketViewSet, PassengerViewSet,BaggageViewSet, AirportViewSet, PositionViewSet, RouteViewSet, StaffViewSet, passenger_report, flight_report, ticket_report, passenger_report, airplane_report, baggage_report, airport_report, position_report, route_report, staff_report
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'airplanes', AirplaneViewSet)
router.register(r'flights', FlightViewSet)
router.register(r'tickets', TicketViewSet)
router.register(r'passengers', PassengerViewSet)
router.register(r'baggages', BaggageViewSet)
router.register(r'airports', AirportViewSet)
router.register(r'positions', PositionViewSet)
router.register(r'routes', RouteViewSet)
router.register(r'staff', StaffViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('flight-report/', flight_report, name = 'flight_report'),
    path('passenger-report/', passenger_report, name = 'passenger_report'),
    path('ticket-report/', ticket_report, name = 'ticket_report'),
    path('airplane-report/', airplane_report, name = 'airplane_report'),
    path('baggage-report/', baggage_report, name = 'baggage_report'),
    path('airport-report/', airport_report, name = 'airport_report'),
    path('position-report/', position_report, name = 'position_report'),
    path('route-report/', route_report, name = 'route_report'),
    path('staff-report/', staff_report, name = 'staff_report'),

    path('api/token/', TokenObtainPairView.as_view(), name = 'token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name = 'token_refresh'),
]