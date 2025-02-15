"""Module providing a Hotel class"""

from src.reservation import Reservation


class Hotel:
    """Hotel class"""

    def __init__(self, name, location, total_rooms):
        self.name = name
        self.location = location
        self.total_rooms = total_rooms
        self.available_rooms = total_rooms
        self.reservations = []

    def modify_hotel(self, name=None, location=None, total_rooms=None):
        """Modify hotel method"""
        if name:
            self.name = name
        if location:
            self.location = location
        if total_rooms is not None:
            self.total_rooms = min(self.available_rooms, total_rooms)

    def delete_hotel(self):
        """Delete hotel method"""
        for reservation in self.reservations:
            reservation.cancel()
        self.reservations.clear()
        self.available_rooms = self.total_rooms

    def reserve_room(self, customer):
        """Reserve room method"""
        if self.available_rooms > 0:
            reservation = Reservation(customer, self)
            self.reservations.append(reservation)
            self.available_rooms -= 1
            return reservation

        print("Error: No available rooms at this hotel.")
        return None

    def cancel_reservation(self, reservation):
        """Cancel reservation method"""
        if reservation in self.reservations:
            reservation.cancel()
            self.reservations.remove(reservation)
            self.available_rooms += 1

    def __str__(self):
        return (
            f"Hotel: {self.name}, Location: {self.location}, "
            f"Available Rooms: {self.available_rooms}/{self.total_rooms}"
        )
