# Sep 6, 2019
# Vitamins
'''
1. a. [1, 2, 3, 4]
   b. 'aBc'
   c. 'ABC'
   d. 'Inside func lst = [1, 2, 3, 4]'
      [1, 2, 3, 4]
   e. 'Inside func s = ABC'
      abc

2. 16 18
   Peter Parker 18
   student 16
   Name: Peter Parker
   Age: 16
   Courses:
   
   Name: Peter Parker
   Age: 16
   Courses: Algebra, Chemistry

   Course Not Found: Spanish

   Removed Couserse": Chmeistry

    ['Algebra', 'Physics', 'Economics']
    ['Algebra', 'Physics', 'Economics']
    Flash Thompson 16
    Peter Parker 18                                                           
   
'''
class Student:
    def __init__(self, name = "student", age = 18):
        self.name = name
        self.age = age
        self.courses = []
    def add_course(self, course):
        self.courses.append(course)
    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
            print("Removed Course:", course)
        else:
            print("Course Not Found:", course)
    def __repr__(self): #str representation needed for print( )
        info = "Name: " + self.name
        info += "\nAge: " + str(self.age)
        info += "\nCourses: " + " , ".join(self.courses)
        return info + "\n"
peter = Student(16)
print(peter.name, peter.age)
peter = Student("Peter Parker")
print(peter.name, peter.age)
peter = Student(age = 16)
print(peter.name, peter.age)
peter.name = "Peter Parker"
print(peter)

peter.add_course("Algebra")
peter.add_course("Chemistry")
print(peter)

peter.add_course("Physics")
peter.remove_course("Spanish")

flash = Student("Flash Thompson")
flash.courses = peter.courses
flash.add_course("Economics")
peter.remove_course("Chemistry")
print(peter.courses)
print(flash.courses)

peter.name, flash.name = flash.name, peter.name
print(peter.name, peter.age)
print(flash.name, flash.age)

def add_binary(bin_num1, bin_num2):
    length=max(len(bin_num1), len(bin_num2))
    carry=0
    result=''
    b1=(length-len(bin_num1))*'0'+bin_num1
    b2=(length-len(bin_num2))*'0'+bin_num2
    for i in range(length):
        add=int(b1[-i])+int(b2[-i])+carry
    result+=str(add)
    return result
print(add_binary('11','1'))
    
    
def can_construct(word, letters):
    char_dict={}
    for char in word:
        if char in char_dict:
            char_dict[char]+=1
        else:
            char_dict[char]=1
    char_dict1={}
    for char in letters:
        if char in char_dict1:
            char_dict1[char]+=1
        else:
            char_dict1[char]=1
    for char in word:
        result=True
        if char_dict[char]!=char_dict1[char]:
            result=False
            break
    return result

#print(can_construct("apples", "aples"))
print(can_construct("apples", "aplespl"))

def create_permutation(n):
    lst=[]
    import random
    for i in range(n):
        num=random.randint(0,n)
        for j in lst:
            if j==num:
                num=random.randint(0,n)
            else:
                lst.append(num)
    return lst
