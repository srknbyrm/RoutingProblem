from dataclasses import dataclass


@dataclass
class DeliveryPoint:
    country: str
    postal_code: str
    latitude: float
    longitude: float
    