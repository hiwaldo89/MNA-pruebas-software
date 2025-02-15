"""Module providing a Customer class"""


class Customer:
    """Customer class"""

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def modify_customer(self, name=None, email=None):
        """Modify Customer Method"""
        if name:
            self.name = name
        if email:
            self.email = email

    def delete_customer(self):
        """Delete Customer Method"""
        self.name = None
        self.email = None

    def __str__(self):
        return f"Customer: {self.name}, Email: {self.email}"
