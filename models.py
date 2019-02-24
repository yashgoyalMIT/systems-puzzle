from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.types import DateTime

class Items(Base):
    """
    Items table
    """
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    quantity = Column(Integer)
    description = Column(String(256))
    date_added = Column(DateTime())

    def serialize(self):
        """ serializes Items into a dictionary """
        return {"id": self.id,
                "name": self.name,
                "quantity": self.quantity,
                "description": self.description}
