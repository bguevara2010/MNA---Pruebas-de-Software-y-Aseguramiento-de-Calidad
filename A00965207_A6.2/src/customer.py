"""Customer module."""

import uuid


class Customer:
    """Represents a customer entity."""

    def __init__(self, name: str, email: str):
        """Initialize a Customer instance."""
        if "@" not in email:
            raise ValueError("Invalid email address")

        self.id = str(uuid.uuid4())
        self.name = name
        self.email = email

    def to_dict(self) -> dict:
        """Return dictionary representation of the customer."""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
        }

    def update_email(self, new_email: str) -> None:
        """Update the customer's email."""
        if "@" not in new_email:
            raise ValueError("Invalid email address")
        self.email = new_email
