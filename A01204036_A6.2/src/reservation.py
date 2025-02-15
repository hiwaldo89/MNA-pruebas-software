"""Module providing a reservation class"""


class Reservation:
    """Reservation class"""

    def __init__(self, customer, hotel):
        self.customer = customer
        self.hotel = hotel
        self.is_canceled = False

    def cancel(self):
        """Cancel reservation method"""
        if self.is_canceled:
            print(f"Reservation for {self.customer.name} is already canceled.")
        else:
            self.is_canceled = True
            print(f"Reservation for {self.customer.name} has been canceled.")

    def __str__(self):
        return (
            f"Reservation for {self.customer.name} "
            f"in {self.hotel.name}"
        )
