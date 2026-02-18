import uuid


class Reservation:
    """Represents a reservation entity."""

    def __init__(self, customer_id: str, hotel_id: str):
        self.id = str(uuid.uuid4())
        self.customer_id = customer_id
        self.hotel_id = hotel_id

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "customer_id": self.customer_id,
            "hotel_id": self.hotel_id,
        }
