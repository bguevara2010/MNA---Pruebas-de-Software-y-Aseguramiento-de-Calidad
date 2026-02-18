import uuid


class Customer:
    """Represents a customer entity."""

    def __init__(self, name: str, email: str):
        if "@" not in email:
            raise ValueError("Invalid email address")

        self.id = str(uuid.uuid4())
        self.name = name
        self.email = email

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
        }
