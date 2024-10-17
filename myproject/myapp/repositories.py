# repositories.py
from .models import Airplane, Airport, Baggage, Flight, Passenger, Position, Route, Staff, Ticket

class AirplaneRepository:
    def get_all(self):
        return Airplane.objects.all()

    def get_by_id(self, airplane_id):
        return Airplane.objects.get(airplaneid=airplane_id)

    def delete(self, airplane_id):
        airplane = Airplane.objects.get(airplaneid=airplane_id)
        airplane.delete()


class AirportRepository:
    def get_all(self):
        return Airport.objects.all()

    def get_by_id(self, airport_id):
        return Airport.objects.get(airportid=airport_id)

    def delete(self, airport_id):
        airport = Airport.objects.get(airportid=airport_id)
        airport.delete()


class BaggageRepository:
    def get_all(self):
        return Baggage.objects.all()

    def get_by_id(self, baggage_id):
        return Baggage.objects.get(baggageid=baggage_id)

    def delete(self, baggage_id):
        baggage = Baggage.objects.get(baggageid=baggage_id)
        baggage.delete()


class FlightRepository:
    def get_all(self):
        return Flight.objects.all()

    def get_by_id(self, flight_id):
        return Flight.objects.get(flightid=flight_id)

    def delete(self, flight_id):
        flight = Flight.objects.get(flightid=flight_id)
        flight.delete()


class PassengerRepository:
    def get_all(self):
        return Passenger.objects.all()

    def get_by_id(self, passenger_id):
        return Passenger.objects.get(passengerid=passenger_id)

    def delete(self, passenger_id):
        passenger = Passenger.objects.get(passengerid=passenger_id)
        passenger.delete()


class PositionRepository:
    def get_all(self):
        return Position.objects.all()

    def create(self, data):
        return Position.objects.create(**data)

    def delete(self, position_id):
        position = Position.objects.get(positionid=position_id)
        position.delete()


class RouteRepository:
    def get_all(self):
        return Route.objects.all()

    def get_by_id(self, route_id):
        return Route.objects.get(routeid=route_id)

    def delete(self, route_id):
        route = Route.objects.get(routeid=route_id)
        route.delete()


class StaffRepository:
    def get_all(self):
        return Staff.objects.all()

    def get_by_id(self, staff_id):
        return Staff.objects.get(staffid=staff_id)

    def delete(self, staff_id):
        staff = Staff.objects.get(staffid=staff_id)
        staff.delete()

class TicketRepository:
    def get_all(self):
        return Ticket.objects.all()

    def get_by_id(self, ticket_id):
        return Ticket.objects.get(ticketid=ticket_id)

    def delete(self, ticket_id):
        ticket = Ticket.objects.get(ticketid=ticket_id)
        ticket.delete()