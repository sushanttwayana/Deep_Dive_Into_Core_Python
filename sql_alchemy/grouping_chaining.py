
from sqlalchemy.orm import sessionmaker
from intro import User, engine
from sqlalchemy import func


Session = sessionmaker(bind=engine)
session = Session()

# group users by age
users = session.query(User.age, func.count(User.name)).group_by(User.age).all()

print(users)

## SQL equivalent

# SELECT age, COUNT(id) FROM users WHERE age > 24 AND age < 50 GROUP BY age ORDER BY "age";

users_tuple = (session.query(User.age, func.count(User.id)).filter((User.age > 24) & (User.age <= 50)).order_by(User.age)
 .group_by(User.age).all()
)

for age, count in users_tuple:
    print(f"Age: {age} - {count} users")


### we can group in this way also

only_batman_dc = False
# only_batman_dc = True
group_by_age = True

users = session.query(User)

if only_batman_dc:
    users = users.filter(User.name == "Batman DC")

if group_by_age:
    users = users.group_by(User.age)

users = users.all()

for user in users:
    print(f"User age: {user.age}, name: {user.name}")