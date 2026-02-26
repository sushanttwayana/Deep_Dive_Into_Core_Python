# Order the data we get from the db using the sql alchemy
from sqlalchemy.orm import sessionmaker
import random
from intro import User, engine

Session = sessionmaker(bind=engine)

session = Session()

### Adding new data to the db randomly

# names = ["Batman DC", "Superman DC", "IronMan Marvel","Hulk Marvel"]
# ages =[20, 30, 40, 50 ,60, 70]

# for x in range(10):
#     user = User(name = random.choice(names), age = random.choice(ages))
#     session.add(user)

# session.commit()

# query all users ordered by age (ascending)
users = session.query(User).order_by(User.age).all()

for user in users:
    print(f"user age: {user.age}, name: {user.name}, id: {user.id}")

print("---------------Printing in descending order-------------")
users = session.query(User).order_by(User.age.desc()).all()

for user in users:
    print(f"user age: {user.age}, name: {user.name}, id: {user.id}")


print("--------------Order by age and name multiple----------")

# query all users ordered by age (ascending)
users = session.query(User).order_by(User.age, User.name).all()

for user in users:
    print(f"user age: {user.age}, name: {user.name}, id: {user.id}")