class Person:
  def __init__(self, name, age):
    #init makes variables name and age inherent when creating the object 
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
print(p1.age)