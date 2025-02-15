"""Main file executing the app"""

from src.customer import Customer
from src.hotel import Hotel

new_customer = Customer("Oswaldo Zarate", "hiwaldo89@gmail.com")
hotel = Hotel("Marriot", "San Jose, CA", 500)

print(new_customer)
print(hotel)

print("Reserve room")
reservation = hotel.reserve_room(new_customer)
print(reservation)
print(hotel)

print("Cancel reservation")
hotel.cancel_reservation(reservation)

print(hotel)
