from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

db_url = 'sqlite:///user_address_database.db'

engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True
    __allow_unmapped__ = True

    id = Column(Integer, primary_key=True)


class Address(BaseModel):
    __tablename__ = 'addresses'

    city = Column(String)
    state = Column(String)
    zip_code = Column(Integer)
    user_id = Column(ForeignKey('users.id'))
    user = relationship('User', back_populates="addresses")

    def __repr__(self):
        return f"<Address (id={self.id}, city='{self.city}')>"


class User(BaseModel):
    __tablename__ = 'users'

    name = Column(String)
    age = Column(Integer)
    addresses = relationship(Address)

    def __repr__(self):
        return f"<User(id={self.id}, age='{self.age}')>"


Base.metadata.create_all(engine)
session = Session()

# If there is data in the db, donot add more data
# creating Users
if session.query(User).count() < 1:
    user1 = User(name="Martin Shrestha", age=25)
    user2 = User(name="Abhay Shrestha", age=23)

    # creating addresses
    address1 = Address(city="Bhaktapur", state = "BK", zip_code = "44800")
    address2 = Address(city="Kathmandu", state = "KT", zip_code = "44600")
    address3 = Address(city="Gorkha", state = "GO", zip_code = "34000")

    # associating address with users
    user2.addresses.extend([address2, address3])
    user1.addresses.append(address1)

    # Adding users and addresses to the session and commiting changes to the db
    session.add(user1)
    session.add(user2)
    session.commit()

address1 = session.query(Address).order_by(Address.id).first()
user1, user2 = session.query(User).limit(2).all()

print(f'address1: {address1.user = }')
print(f'user1:    {user1.addresses = }')
print(f'user2:    {user2.addresses = }')