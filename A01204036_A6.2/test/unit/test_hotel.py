"""Hotel class test"""

import unittest
from unittest.mock import MagicMock, patch
from src.hotel import Hotel


class TestHotel(unittest.TestCase):
    """Test case for Hotel class"""

    def setUp(self):
        """Set up test variables"""
        self.customer = MagicMock()
        self.customer.name = "Oswaldo Zarate"
        self.hotel = Hotel(name="Marriot",
                           location="San Jose, CA", total_rooms=5)

    def test_initialization(self):
        """Test initialization of Hotel class"""
        self.assertEqual(self.hotel.name, "Marriot")
        self.assertEqual(self.hotel.location, "San Jose, CA")
        self.assertEqual(self.hotel.total_rooms, 5)
        self.assertEqual(self.hotel.available_rooms, 5)
        self.assertEqual(len(self.hotel.reservations), 0)

    def test_modify_hotel(self):
        """Test modify hotel method"""
        self.hotel.modify_hotel(name="Luxury Hotel",
                                location="San Francisco, CA", total_rooms=10)
        self.assertEqual(self.hotel.name, "Luxury Hotel")
        self.assertEqual(self.hotel.location, "San Francisco, CA")
        self.assertEqual(self.hotel.total_rooms, 5)

    def test_cancel_reservation(self):
        """Test cancel reservation method"""
        reservation = self.hotel.reserve_room(self.customer)
        self.assertIn(reservation, self.hotel.reservations)
        self.assertEqual(self.hotel.available_rooms, 4)
        self.hotel.cancel_reservation(reservation)
        self.assertNotIn(reservation, self.hotel.reservations)
        self.assertEqual(self.hotel.available_rooms, 5)

    def test_reserve_room_when_no_rooms_available(self):
        """Test reserve room method when no rooms are available"""
        for _ in range(5):
            self.hotel.reserve_room(self.customer)

        with patch("builtins.print") as mocked_print:
            reservation = self.hotel.reserve_room(self.customer)

            mocked_print.assert_called_with(
                "Error: No available rooms at this hotel.")
            self.assertIsNone(reservation)
            self.assertEqual(self.hotel.available_rooms, 0)
            self.assertEqual(len(self.hotel.reservations), 5)

    def test_delete_hotel(self):
        """Test delete hotel method"""
        self.hotel.reserve_room(self.customer)
        self.hotel.delete_hotel()
        self.assertEqual(self.hotel.available_rooms, 5)
        self.assertEqual(len(self.hotel.reservations), 0)

    def test_str(self):
        """Test the string representation of the Hotel"""
        expected_str = (
            "Hotel: Marriot, "
            "Location: San Jose, CA, "
            "Available Rooms: 5/5"
        )
        self.assertEqual(str(self.hotel), expected_str)
