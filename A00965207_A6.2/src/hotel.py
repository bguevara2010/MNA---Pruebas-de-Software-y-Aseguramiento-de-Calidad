"""Hotel module."""

import uuid


class Hotel:
    """Represents a hotel entity."""

    def __init__(self, name: str, location: str, rooms: int):
        """Initialize a Hotel instance."""
        if rooms <= 0:
            raise ValueError("Rooms must be greater than zero")

        self.id = str(uuid.uuid4())
        self.name = name
        self.location = location
        self.rooms = rooms

    def to_dict(self) -> dict:
        """Return dictionary representation of the hotel."""
        return {
            "id": self.id,
            "name": self.name,
            "location": self.location,
            "rooms": self.rooms,
        }

    def update_rooms(self, new_rooms: int) -> None:
        """Update the number of rooms."""
        if new_rooms <= 0:
            raise ValueError("Rooms must be greater than zero")
        self.rooms = new_rooms
