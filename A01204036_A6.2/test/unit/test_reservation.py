"""Reservation class test"""

import unittest
from unittest.mock import MagicMock, patch
from src.reservation import Reservation


class TestReservation(unittest.TestCase):
    """Test case for Reservation class"""

    def setUp(self):
        """Set up test variables"""
        self.customer = MagicMock()
        self.customer.name = "Oswaldo Zarate"
        self.hotel = MagicMock()
        self.hotel.name = "Marriot"
        self.reservation = Reservation(self.customer, self.hotel)

    def test_initialization(self):
        """Test initialization of Reservation class"""
        self.assertEqual(self.reservation.customer.name, "Oswaldo Zarate")
        self.assertEqual(self.reservation.hotel.name, "Marriot")
        self.assertFalse(self.reservation.is_canceled)

    def test_cancel_reservation(self):
        """Test cancel reservation method"""
        self.reservation.cancel()
        self.assertTrue(self.reservation.is_canceled)

    def test_cancel_reservation_twice(self):
        """Test canceling a reservation twice"""
        with patch('builtins.print') as mocked_print:
            self.reservation.cancel()
            self.reservation.cancel()
            mocked_print.assert_called_with(
                "Reservation for Oswaldo Zarate is already canceled.")

    def test_str(self):
        """Test the string representation of the Reservation"""
        expected_str = "Reservation for Oswaldo Zarate in Marriot"
        self.assertEqual(str(self.reservation), expected_str)
