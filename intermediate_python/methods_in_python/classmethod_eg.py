from itertools import count


class Student:

    total_gpa = 0
    count = 0


    def __init__(self, name:str, gpa:float) -> None:
        
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # Instance Method
    def get_info(self):

        """
            This is the instance method 
        """
        return f"{self.name} {self.gpa}"


    # class method
    @classmethod
    def get_count(cls):
        """
            This is the first classmethod of get_count which will return the total count of students
        """

        return f"Total number of students: {cls.count}"


    @classmethod
    def get_average_gpa(cls):
        
        if cls.count == 0:
            return 0 

        else:
            return f"{cls.total_gpa / cls.count: .3f}"

student1 = Student("Ram", 3.40)
student1 = Student("Hari", 3.21)
student1 = Student("Sita", 3.72)


print(Student.get_count())
print(Student.get_average_gpa())