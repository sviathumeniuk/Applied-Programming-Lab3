from .repositories import AirplaneRepository, AirportRepository, BaggageRepository, FlightRepository, PassengerRepository, PositionRepository, RouteRepository, StaffRepository, TicketRepository

class RepositoryFacade:
    def __init__(self):
        self.airplane_repo = AirplaneRepository()
        self.airport_repo = AirportRepository()
        self.baggage_repo = BaggageRepository()
        self.flight_repo = FlightRepository()
        self.passenger_repo = PassengerRepository()
        self.position_repo = PositionRepository()
        self.route_repo = RouteRepository()
        self.staff_repo = StaffRepository()
        self.ticket_repo = TicketRepository()

    # Методи для взаємодії з Airplane
    def get_all_airplanes(self):
        return self.airplane_repo.get_all()

    def get_airplane_by_id(self, airplane_id):
        return self.airplane_repo.get_by_id(airplane_id)

    def delete_airplane(self, airplane_id):
        return self.airplane_repo.delete(airplane_id)

    # Методи для взаємодії з Airport
    def get_all_airports(self):
        return self.airport_repo.get_all()

    def get_airport_by_id(self, airport_id):
        return self.airport_repo.get_by_id(airport_id)
    
    def delete_airport(self, airport_id):
        return self.airport_repo.delete(airport_id)

    # Методи для Baggage
    def get_all_baggages(self):
        return self.baggage_repo.get_all()

    def get_baggage_by_id(self, baggage_id):
        return self.baggage_repo.get_by_id(baggage_id)

    def delete_baggage(self, baggage_id):
        return self.baggage_repo.delete(baggage_id)

    # Методи для Flight
    def get_all_flights(self):
        return self.flight_repo.get_all()

    def get_flight_by_id(self, flight_id):
        return self.flight_repo.get_by_id(flight_id)

    def delete_flight(self, flight_id):
        return self.flight_repo.delete(flight_id)

    # Методи для Passenger
    def get_all_passengers(self):
        return self.passenger_repo.get_all()

    def get_passenger_by_id(self, passenger_id):
        return self.passenger_repo.get_by_id(passenger_id)

    def delete_passenger(self, passenger_id):
        return self.passenger_repo.delete(passenger_id)

    # Методи для Position
    def get_all_positions(self):
        return self.position_repo.get_all()

    def delete_position(self, position_id):
        return self.position_repo.delete(position_id)

    # Методи для Route
    def get_all_routes(self):
        return self.route_repo.get_all()

    def get_route_by_id(self, route_id):
        return self.route_repo.get_by_id(route_id)

    def delete_route(self, route_id):
        return self.route_repo.delete(route_id)

    # Методи для Staff
    def get_all_staff(self):
        return self.staff_repo.get_all()

    def get_staff_by_id(self, staff_id):
        return self.staff_repo.get_by_id(staff_id)

    def delete_staff(self, staff_id):
        return self.staff_repo.delete(staff_id)

    # Методи для Ticket
    def get_all_tickets(self):
        return self.ticket_repo.get_all()

    def get_ticket_by_id(self, ticket_id):
        return self.ticket_repo.get_by_id(ticket_id)

    def delete_ticket(self, ticket_id):
        return self.ticket_repo.delete(ticket_id)