import unittest
from src.customer import Customer


class TestCustomer(unittest.TestCase):
    """Unit tests for Customer class."""

    def test_create_customer(self):
        customer = Customer("Bruno", "bruno@email.com")
        self.assertEqual(customer.name, "Bruno")
        self.assertEqual(customer.email, "bruno@email.com")
        self.assertIsNotNone(customer.id)

    def test_invalid_email(self):
        with self.assertRaises(ValueError):
            Customer("Bruno", "invalid-email")

    def test_to_dict(self):
        customer = Customer("Ana", "ana@email.com")
        customer_dict = customer.to_dict()
        self.assertIn("id", customer_dict)
        self.assertEqual(customer_dict["name"], "Ana")
        self.assertEqual(customer_dict["email"], "ana@email.com")
