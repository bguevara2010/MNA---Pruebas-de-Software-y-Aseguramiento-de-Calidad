"""Reservation module."""

import uuid


class Reservation:
    """Represents a reservation entity."""

    def __init__(self, customer_id: str, hotel_id: str):
        """Initialize a Reservation instance."""
        self.id = str(uuid.uuid4())
        self.customer_id = customer_id
        self.hotel_id = hotel_id

    def to_dict(self) -> dict:
        """Return dictionary representation of the reservation."""
        return {
            "id": self.id,
            "customer_id": self.customer_id,
            "hotel_id": self.hotel_id,
        }

    def change_hotel(self, new_hotel_id: str) -> None:
        """Change the hotel associated with the reservation."""
        self.hotel_id = new_hotel_id
