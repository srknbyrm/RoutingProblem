from sqlalchemy import Column, Integer, ForeignKey
from . import Base


class LocationRoute(Base):
    __tablename__ = "location_route"
    id = Column(Integer, primary_key=True)
    order_no = Column(Integer, nullable=False)
    fk_location_id = Column(Integer, ForeignKey('locations.id'))
    fk_route_id = Column(Integer, ForeignKey('route.id'))

    def __init__(self, order_no, fk_location_id, fk_route_id):
        self.order_no = order_no
        self.fk_location_id = fk_location_id
        self.fk_route_id = fk_route_id

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
