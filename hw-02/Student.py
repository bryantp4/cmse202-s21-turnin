# The Student class (you'll edit and expand on this)
class Student():
    '''
    This class is designed to include information about individual students.
    Currently this class has the following attributes:
    
    name : this is the student's name
    gpa : this is the student's curret gpa
    year : this is the student's year in college
    '''
    
    def __init__(self, name='', gpa=0.0, year=1):
        self.name = name
        self.gpa = gpa
        self.year = year
        
    def get_name(self):
        '''
        This function prints the name of the student
        '''
        print("My name is", self.name)
    
    def enroll(self, courses):
        self.courses = courses
    
    def display_courses(self):
        print("I am enrolled in", self.courses)
        
    def years_until_graduation(self):
        grad = 4 - self.year
        return grad
    

class Spartan(Student):
    '''
    This class was created to inherit the student class, as well as
    have a few different attributes
    '''
    
    def __init__(self, name=''):
        super().__init__(self, name=''):
        
    def set_motto(self, motto):
        self.motto = motto
        
    def school_spirit(self):
        print(Student.get_name())
        print("I am a Spartan. My motto is", self.motto)