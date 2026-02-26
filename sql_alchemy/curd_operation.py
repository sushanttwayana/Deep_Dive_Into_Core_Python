from sqlalchemy.orm import sessionmaker

from intro import engine, User

Session = sessionmaker(bind=engine)

session = Session()

#------------------------- add data to the database

user = User(name="John Cena", age=50)
user_2 = User(name="Randy Orton", age=45)
user_3 = User(name="The Rock", age=55)
user_4 = User(name="Seth Rollins", age=40)
user_5 = User(name="Dean Ambrose", age=45)

session.add(user)
session.add(user_2)

# we can use session.add_all() to add multiple users at once
session.add_all([user_3, user_4, user_5])

session.commit()

# access / Read the data from the database

users = session.query(User).all()

print(users[0])

user = users[0]

print(user.id)
print(user.name)
print(user.age)

# looping through to get the data

for user in users:
    print(f"User id:{user.id}, Name:{user.name}, Age:{user.age}")

# --------------------------

# user = session.query(User).filter_by(id=1).one_or_none()
user = session.query(User).filter_by(id=1).all()
user = session.query(User).filter_by(id=1).first()

print(user)
print(user.name)
print(user.age)
print(user.id)

## Updating the records in the db
user.name = "Batista Bum"
print(user.name)

# this is save our changes and reflect it back to the db
session.commit()


# Delete the record from the db

user1 = session.query(User).filter_by(id = 1).one_or_none()

session.delete(user1)

session.commit()
