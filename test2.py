class Student:

    def __init__(self, name, age ): # python class constructor

        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello! My name is " + self.name)








print("******** Test 2 **********")

student1 = Student("Corey Arnold", 27)
student1.say_hello()

student2 = Student("Chris Daming", 24)
student2.say_hello()


print(student1.name) # get data out of object
student1.name = "Jameson Haeden"
print(student1.name)




me = {
    "name": "Corey",
    "age": 27
}
print(type(student1)) # check what type you are using
print(type(me))
print(me["name"])



