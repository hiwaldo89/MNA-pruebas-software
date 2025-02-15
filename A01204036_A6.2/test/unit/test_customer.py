"""Customer class test"""

import unittest
from src.customer import Customer


class TestCustomer(unittest.TestCase):
    """Test case for Customer class"""

    def setUp(self):
        """Set up test variables"""
        self.customer = Customer("Oswaldo Zarate", "hiwaldo89@gmail.com")

    def test_initialization(self):
        """Test initialization of Customer class"""
        self.assertEqual(self.customer.name, "Oswaldo Zarate")
        self.assertEqual(self.customer.email, "hiwaldo89@gmail.com")

    def test_modify_customer(self):
        """Test modify customer method"""
        self.customer.modify_customer("Areli Velazquez")
        self.assertEqual(self.customer.name, "Areli Velazquez")
        self.assertEqual(self.customer.email, "hiwaldo89@gmail.com")
        self.customer.modify_customer(email="areli.vela@gmail.com")
        self.assertEqual(self.customer.name, "Areli Velazquez")
        self.assertEqual(self.customer.email, "areli.vela@gmail.com")

    def test_delete_customer(self):
        """Test delete customer method"""
        self.customer.delete_customer()
        self.assertIsNone(self.customer.name)
        self.assertIsNone(self.customer.email)

    def test_str(self):
        """Test the string representation of the Customer"""
        expected_str = "Customer: Oswaldo Zarate, Email: hiwaldo89@gmail.com"
        self.assertEqual(str(self.customer), expected_str)
