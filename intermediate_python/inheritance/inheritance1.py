from inspect import AGEN_CLOSED


class Person:
    
    def __init__(self, name, age, height) -> None:
        self.name = name
        self.age = age
        self.height = height

    def __str__(self) -> str:
        return "Name: {}, Age: {}, Height: {}".format(self.name, self.age, self.height)

    def get_older(self, years):
        self.age += years
    
class Worker(Person):

    def __init__(self, name, age, height, salary) -> None:
        super(Worker, self).__init__(name, age, height)
        self.salary = salary

    def __str__(self) -> str:

        # text = super(Wo)
        text = super(Worker, self).__str__()
        text += ", Salary in Rs.{}".format(self.salary)

        return text

    def calc_yearly_salary(self):
        return self.salary * 12


worker1 = Worker("Mark", 30, 180, 30000)
print(worker1)
print(worker1.calc_yearly_salary())
