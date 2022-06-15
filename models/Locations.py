from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from . import Base


class Location(Base):
    __tablename__ = "locations"
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    route_location = relationship('LocationRoute', backref='Location')

    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return "<Location(name='%s', latitude='%s', longitude='%s')>" % (self.name, self.latitude, self.longitude)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}