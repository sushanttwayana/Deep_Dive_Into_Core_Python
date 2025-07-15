import threading

def function_one():
    for i in range(10000):
        print("ONE")

def function_two():
    for i in range(10000):
        print("TWO")


t1 = threading.Thread(target=function_one)
t2 = threading.Thread(target=function_two)

t1.start()
t2.start()

# function_one()
# function_two()
