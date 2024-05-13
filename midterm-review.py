

""" x = input("Enter a Number")

tek mi çift mi?

if (int(x) % 2 ==0):
  print('Even')
else :
  print ('Odd')

 """

""" 
3 tane not al ve bunların ortalamasını çıkar sonra da 90dan fazlaysa burs ver

sum = 0
average = 0

grade_1 = input ('First students grade : ')
grade_2 = input ('Second students grade : ')
grade_3 = input ('Third students grade : ')

sum = int(grade_1)+int(grade_2)+int(grade_3)

average = int(sum) / 3.0

if (average > 90):
  print("Congrats! You have won a scholarship!")
else:
  print("Your average is : ",average)

 """
""" for i in range (3):
  username= input('Please enter username: ')
  password= input('Please enter password: ')
  if(username == "admin" and password == "1234" and i <3):
    print("Login successful")
  elif(i<3):
    print("wrong user name or password")
  elif(i==3):
    print("BLOCKED")

 """
""" for i in range(1,100,2):
  print(i) """

#functıons


""" def hello(name):
  print('annen' + name)
  print('bacın')

hello("yarram")

 """

""" def multiply(number1,number2):
  return number1*number2



print(multiply(3,9))

 """

""" 
def main():
  value=99
  print("The value is ", value)
  change_me(value)
  print('Back in the main value is ',value)


def change_me(arg):
  print('I am changin the value.')
  arg=0
  print('Now the value is ',arg)


main() """

#KEYWORD ARGS

""" def hello(first,middle,last):
  print("Hello " + str(first)+ " " + str(middle)+" " + str(last))


hello(last="ece",first="gozde",middle="caliskan")

 """
""" 
def greeting():
  first_name=input("Hello, please give us your name: ")
  last_name=input("And your last name: ")
  print("Welcome " + str(first_name) + " " + str(last_name))

greeting()
 """


""" 
def foo (x,y) :
  def bar (z) :
    return z * 2
  return bar(x) + y

foo(2,3) """

""" def welcome_guest():
    print("Hello, welcome to our hotel!")

    def hotel_info():
        hotel_name = "Luxury Inn"
        year_established = 1990
        print(f"Hotel Name: {hotel_name}")
        print(f"Year Established: {year_established}")
  

    # Call the internal function
    hotel_info()

# Call the outer function
welcome_guest()
 """

""" import random


x=random.randint(1,6) #1,6 arası verir
y=random.randint() #0-1 arası verir


print(x) """


""" class Phone:
  

  def __init__(self,model,name,year):
    self.model=model
    self.name=name
    self.year=year

  def working(self):
    print(self.model + " "+ self.name + " is working now")

  def stop(self):
    print("Phone has stopped working")



phone1 = Phone("Apple","iPhone Pro 15","2023")

print(phone1.model)

phone1.working()
phone1.stop()
 """
"""     
class Coordinate():
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def distance(self,other):
    x_diff_eq = (self.x - other.x)**2
    y_diff_eq = (self.y - other.y)**2
    return (x_diff_eq+y_diff_eq)**0.5
  

c = Coordinate (3,4)
zero = Coordinate(0,0)

print(c.distance(zero))

 """

""" class Animal():
  def __init__(self,age,name = None):
    self.age = age
    self.name = name if name is not None else " "

  def get_age(self):
    return self.age
  def get_name (self):
    return self.name 

  def set_age(self,new_age):
    self.age = new_age
  def set_name(self,new_name):
    self.name = new_name

  def __str__ (self):
    return f"Name: {self.name}, Age: {self.age}"



animal1 = Animal(2)
animal2= Animal(9)



animal2.set_name("Lucky")

print(animal2) """



class Employee():

  def __init__ (self,name,salary):
    self.name=name
    self.salary=salary

  def get_name(self):
    return self.name

  def get_salary(self):
    return self.salary

class SalesOfficer(Employee):
  def __init__(self,name,salary,raise_percentage):
    Employee.__init__(self,name,salary)
    self.raise_percentage=raise_percentage

  def get_salary(self):
    increased_Salary = self.salary + (self.salary * (self.raise_percentage/100))
    return increased_Salary


e= Employee("Mehmetcan",10000)
s=SalesOfficer("Ali",1500,10)


print(s.get_salary())









