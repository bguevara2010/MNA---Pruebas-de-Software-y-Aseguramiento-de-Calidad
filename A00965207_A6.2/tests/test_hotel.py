import unittest
from src.hotel import Hotel


class TestHotel(unittest.TestCase):

    def test_create_hotel(self):
        hotel = Hotel("Marriott", "NY", 100)
        self.assertEqual(hotel.name, "Marriott")

    def test_invalid_rooms(self):
        with self.assertRaises(ValueError):
            Hotel("Test", "NY", 0)
