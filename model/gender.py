from base import Base
from sqlalchemy import Column, String, Integer

class Gender(Base):
    __tablename__ = 'gender'

    def __init__(self, id, name):
        super(Gender, self).__init__()

        self.id = int(id)
        self.name = name

    id = Column(Integer, primary_key=True)
    name = Column(String(6))

    # visitor_gender = relationship("Visitor", backref="gender", order_by="Visitor.id")

    # @staticmethod
    # def find_all():
    #     genders = []
    #     g = session.query(Gender.id, Gender.name)
    #     for gender in g:
    #         object_gender = Gender(gender[0], gender[1])
    #         genders.append(object_gender)
    #     return genders