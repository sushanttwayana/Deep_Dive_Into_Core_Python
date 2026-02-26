from one_to_many_reln import Address, session, User

# creating Users
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

print(f"{user1.addresses = }")
print(f"{user2.addresses = }")