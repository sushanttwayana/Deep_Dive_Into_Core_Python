# class A:
#     def display(self):
#         print("Display from class A")

# class B(A):
#     def display(self):
#         print("Display from class B")

# class C(A):

#     def show(self):
#         print("Hi from class C")

#     def display(self):
#         print("Display from class C")

# class D(B, C):

#     pass


# d1 = D()
# print(d1.display())

# # print(D.mro())
# print(D.__mro__)


class A:

    def show(self): 
        print("hello A")
class B(A):

    def show(self):
       print("hello B")

class C(A):

    def show(self):
        print("hello C")

class D(A, B):
    pass

d = D()
d.show()