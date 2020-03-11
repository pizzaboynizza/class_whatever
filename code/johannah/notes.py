class Dog():
  #init method is called automatically right after the object has been created. once we initialize the object we call this method automatically
  #each attribute in a class definition begins with a reference to the instance object and that is the 'self' keyword which is basically saying refer to this particular instance of this object


  # CLASS OBJECT ATTRIBUTE
  species = "mammal"
  
  def __init__(self,breed,name): # breed and name are attributes
    self.breed = breed
    self.name = name  # this name refers to the inout 'name' 2 lines above
    # these are saying 'self' which refers to class Dog(), .name(or .breed or whatever attribute) which is going to be the name (or breed, etc) in the def __init__(...)
  def breed_type(self,breedtype)
mydog = Dog(breed = "Lab",name="Sammy")
#the "breed" is the argument and the value is passed during th]e instantiation or initialization of the class itself where we say: breed = "Lab" . And now we've created an instance of the dog class
otherdog = Dog(breed="Husky")
#another instance (otherdog)
# print(type(mydog))
otherdog.breedtype(otherdog)                              # "" is now the new self
print(mydog.breed)
print(mydog.name)
print(mydog.species)
print(otherdog.breed)


class Circle():

  pi = 3.14

  def __init__(self,radius=1):  # if I don't provide a radius I will provide the default value of 1
    self.radius = radius  # this means Circle.radius is going to equal the input radius

  # create a method that calculates the area of a circle(methods are functions defined inside the body of a class that allow us to perform actions based off the attributes of the object)
  def area(self):  # this tells the method 'area' that it's not just some free floating function inside of this class, it's actually a method of that class and that's what the self keyword is doing
    return self.radius*self.radius * Circle.pi   # pi is an object level attribute

# now let's create an instance of Circle:
myc = Circle(3)  # radius is 3
print(myc.area())

# a method that allows me to reset the radius 
# there's 2 ways you can change attributes of a class: 1 way is to just call it directly off the object itself
myc.radius = 100
print(myc.area())

def set_radius(self,new_r):   # new_r is a parameter
  self.radius = new_r   # not all object methods need to retun something, some object methods just affect the object in place

myc.set_radius(100)