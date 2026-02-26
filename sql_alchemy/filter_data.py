import random

from sqlalchemy.orm import sessionmaker
from intro import User, engine
from sqlalchemy import or_, and_, not_

Session = sessionmaker(bind=engine)
session = Session()

# query all users
users_all = session.query(User).all()

# query all users with age greater than or equal to 25
# users_filtered = session.query(User).filter(User.age >= 25).all()
users_filtered = session.query(User).filter(User.name == "Batman DC").all()

# print("All Users:", len(users_all))
# print("Filtered Users:", len(users_filtered))


## where method

users_30 = session.query(User).where(User.age >= 30).all()

for user in users_30:
    print(f"User age: {user.age}")

# AND function in sql alchemy
users_30_Batman_DC = session.query(User).where(User.age >= 30, User.name == "Batman DC").all()

for user in users_30_Batman_DC:
    print(f"User age: {user.age}")

# OR function in sql alchemy

users_or = session.query(User).where(or_(User.age >= 30, User.name == "Batman DC")).all()
users_or = session.query(User).where(and_(User.age >= 30, User.name == "Batman DC")).all()

for user in users_or:
    print(f"{user.age} - {user.name}")

# Similarly using bitwise operator

users_or = session.query(User).where((User.age >= 30) | (User.name == "Batman DC")).all()
users_or = session.query(User).where((User.age >= 30) & (User.name == "Batman DC")).all()


print("--------Using bitwise OR operator--------")
for user in users_or:
    print(f"{user.age} - {user.name}")



### ----------------

print("------------------Final Combined-----------------")

users_new = (
    session.query(User).where(
        or_(
            not_(User.name == "Batman DC"),
            and_(
                User.age > 30,
                User.age < 50
            )
        )
    )
).all()

for user in users_new:
    print(f"{user.age} - {user.name}")