from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Count
from .serializers import AirplaneSerializer, FlightSerializer, TicketSerializer, PassengerSerializer, BaggageSerializer, AirportSerializer, PositionSerializer, RouteSerializer, StaffSerializer
from .facade import RepositoryFacade
from rest_framework.permissions import IsAuthenticated

facade = RepositoryFacade()

class AirplaneViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = facade.get_all_airplanes()
    serializer_class = AirplaneSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def list(self, request):
        airplanes = facade.get_all_airplanes()
        serializer = AirplaneSerializer(airplanes, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        airplane = facade.get_airplane_by_id(pk)
        serializer = AirplaneSerializer(airplane)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        facade.delete_airplane(pk)
        return Response(status=204)
    
class StaffViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = facade.get_all_staff()
    serializer_class = StaffSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def list(self, request):
        staff = facade.get_all_staff()
        serializer = StaffSerializer(staff, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        staff = facade.get_staff_by_id(pk)
        serializer = StaffSerializer(staff)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        facade.delete_staff(pk)
        return Response(status=204)

class PositionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = facade.get_all_positions()
    serializer_class = PositionSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def list(self, request):
        positions = facade.get_all_positions()
        serializer = PositionSerializer(positions, many=True)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        facade.delete_position(pk)
        return Response(status=204)

class AirportViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = facade.get_all_airports()
    serializer_class = AirportSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def list(self, request):
        airports = facade.get_all_airports()
        serializer = AirportSerializer(airports, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        airport = facade.get_airport_by_id(pk)
        serializer = AirportSerializer(airport)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        facade.delete_airport(pk)
        return Response(status=204)

class FlightViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = facade.get_all_flights()
    serializer_class = FlightSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def list(self, request):
        flights = facade.get_all_flights()
        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        flight = facade.get_flight_by_id(pk)
        serializer = FlightSerializer(flight)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        facade.delete_flight(pk)
        return Response(status=204)
    
class TicketViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = facade.get_all_tickets()
    serializer_class = TicketSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def list(self, request):
        tickets = facade.get_all_tickets()
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        ticket = facade.get_ticket_by_id(pk)
        serializer = TicketSerializer(ticket)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        facade.delete_ticket(pk)
        return Response(status=204)

class PassengerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = facade.get_all_passengers()
    serializer_class = PassengerSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def list(self, request):
        passengers = facade.get_all_passengers()
        serializer = PassengerSerializer(passengers, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        passenger = facade.get_passenger_by_id(pk)
        serializer = PassengerSerializer(passenger)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        facade.delete_passenger(pk)
        return Response(status=204)

class BaggageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = facade.get_all_baggages()
    serializer_class = BaggageSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def list(self, request):
        baggages = facade.get_all_baggages()
        serializer = BaggageSerializer(baggages, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        baggage = facade.get_baggage_by_id(pk)
        serializer = BaggageSerializer(baggage)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        facade.delete_baggage(pk)
        return Response(status=204) 
    
class RouteViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = facade.get_all_routes()
    serializer_class = RouteSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def list(self, request):
        routes = facade.get_all_routes()
        serializer = RouteSerializer(routes, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        route = facade.get_route_by_id(pk)
        serializer = RouteSerializer(route)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        facade.delete_route(pk)
        return Response(status=204) 

@api_view(['GET'])
def flight_report(request):
    report = facade.flight_repo.get_all().aggregate(total_flights=Count('flightid'))
    return Response(report)

@api_view(['GET'])
def passenger_report(request):
    report = facade.passenger_repo.get_all().aggregate(total_passengers=Count('passengerid'))
    return Response(report)

@api_view
def ticket_report(request):
    report = facade.ticket_repo.get_all().aggregate(total_tickets=Count('ticketid'))
    return Response(report)

@api_view
def airplane_report(request):
    report = facade.airplane_repo.get_all().aggregate(total_airplanes=Count('airplaneid'))
    return Response(report)

@api_view
def baggage_report(request):
    report = facade.baggage_repo.get_all().aggregate(total_baggage=Count('baggageid'))
    return Response(report)

@api_view
def airport_report(request):
    report = facade.airport_repo.get_all().aggregate(total_airports=Count('airportid'))
    return Response(report)

@api_view
def position_report(request):
    report = facade.position_repo.get_all().aggregate(total_positions=Count('positionid'))
    return Response(report)

@api_view
def route_report(request):
    report = facade.route_repo.get_all().aggregate(total_route=Count('routeid'))
    return Response(report)

@api_view
def staff_report(request):
    report = facade.staff_repo.get_all().aggregate(total_staff = Count('staffid'))
    return Response(report)