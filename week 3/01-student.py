""" 
Object - encapsulates state (attributes) + behavior (methods)
Class - Template for creating an object
"""
class Student:
    """ 
    __init__ function will automatically execute whenever a new object is created using this class
    
    """
    def __init__(self):
        print("a new student object is created")
        self.id = 0
        self.name = ""
        self.location = ""
        
    def whoAmI(self):
        print(f"Id={self.id}, Name={self.name}, Location={self.location}")


# creating a new Student object
s1 = Student() 

# Assign the values to the attributes
s1.id = 101
s1.name = "Magesh"
s1.location = "Bangalore"

# accessing the attributes (state)
""" 
print(s1.id)
print(s1.name)
print(s1.location)
"""

# method invocation
s1.whoAmI()



s2 = Student() # creating another new Student object
s2.id = 102
s2.name = "Suresh"
s2.location = "Chennai"
s2.whoAmI()

s3 = Student() # creating another new Student object
s3.id = "103"
s3.name = "Rajesh"
s3.location = "Villivakkam"
s3.whoAmI()