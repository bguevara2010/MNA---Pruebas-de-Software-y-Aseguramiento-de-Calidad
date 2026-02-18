import unittest
from src.reservation import Reservation


class TestReservation(unittest.TestCase):
    """Unit tests for Reservation class."""

    def test_create_reservation(self):
        reservation = Reservation("cust123", "hotel456")
        self.assertEqual(reservation.customer_id, "cust123")
        self.assertEqual(reservation.hotel_id, "hotel456")
        self.assertIsNotNone(reservation.id)

    def test_to_dict(self):
        reservation = Reservation("cust1", "hotel1")
        reservation_dict = reservation.to_dict()
        self.assertIn("id", reservation_dict)
        self.assertEqual(reservation_dict["customer_id"], "cust1")
        self.assertEqual(reservation_dict["hotel_id"], "hotel1")
