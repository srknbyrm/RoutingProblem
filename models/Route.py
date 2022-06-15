from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from . import Base


class Route(Base):
    __tablename__ = "route"
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    optimal_solution = Column(Float, nullable=False)
    route_location = relationship('LocationRoute', backref='route')

    def __init__(self, name, optimal_solution):
        self.name = name
        self.optimal_solution = optimal_solution

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
