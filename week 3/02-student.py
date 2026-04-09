""" 
Object - encapsulates state (attributes) + behavior (methods)
Class - Template for creating an object
"""
class Student:
    """ 
    __init__ function will automatically execute whenever a new object is created using this class
    
    """
    def __init__(self, id, name, location):
        print("a new student object is created")
        self.id = id
        self.name = name
        self.location = location
        
    def whoAmI(self):
        print(f"Id={self.id}, Name={self.name}, Location={self.location}")


# creating a new Student object with the given state
s1 = Student(100, "Magesh", "Bangalore") 



# accessing the attributes (state)
""" 
print(s1.id)
print(s1.name)
print(s1.location)
"""

# method invocation
s1.whoAmI()

# creating another new Student object
s2 = Student(102, "Suresh", "Chennai") 
s2.whoAmI()

# creating another new Student object
s3 = Student(103, "Rajesh", "Villivakkam") 
s3.whoAmI()