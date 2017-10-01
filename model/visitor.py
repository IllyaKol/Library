from base import Base
from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship


class Visitor(Base):
    __tablename__ = 'visitor'

    def __init__(self, id, name, last_name, birth_date, number, gender_id):
        super(Visitor, self).__init__()

        self.id = id
        self.name = name
        self.last_name = last_name
        self.birth_date = birth_date
        self.number = number
        self.gender_id = gender_id

    id = Column(Integer, primary_key=True)
    name = Column(String(15))
    last_name = Column(String(25))
    birth_date = Column(Date)
    number = Column(String(20))
    gender_id = Column(ForeignKey('gender.id'))

    book_in_visitor = relationship("BookInVisitor", backref="visitor", order_by="BookInVisitor.id")
    gender = relationship("Gender", backref="visitor", order_by="Gender.id")
    history = relationship('BookInVisitor')

    # @staticmethod
    # def find_all():
    #     visitors = []
    #     vs = session.query(Visitor.id, Visitor.name, Visitor.last_name, Visitor.birth_date, Visitor.number, Visitor.gender_id)
    #     for visitor in vs:
    #         visitor = Visitor(visitor[0], visitor[1], visitor[2], visitor[3], visitor[4], visitor[5])
    #         visitors.append(visitor)
    #     return visitors

    # def insert(self):
    #     visitor_object = Visitor(self.id, self.name, self.last_name, self.birth_date, self.number, self.gender_id)
    #     session.add(visitor_object)
    #     session.commit()
        # cursor.execute("INSERT INTO visitor (id, name, last_name, birth_date, number, gender_id) VALUES ({0}, '{1}', '{2}', '{3}', '{4}', {5})".format(self.id, self.name, self.last_name, self.birth_date, self.number, self.gender_id))
        # db.commit()