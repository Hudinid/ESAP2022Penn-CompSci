class Dog():
    #attributes
    #name, breed, color

    #Actions
    #barks
    #wags tail

    #init is also a constructor
    #functions defined within a class are called a method
    def __init__(self, name, breed, color, height, weight):
        self.name = name
        self.breed = breed
        self.color = color
        self.height = height
        self.weight = weight
        self.age = 0
        #self. will create instance variables / class level attributes
    def __str__(self):
        #always remember that you need to return and not print the string version of the object
        return "This is " + self.name + " who is a " + self.breed
    def bark(self):
        #this particular dog is barking
        print(self.name + " is barking")

    def bark_at_dog(self, dog):
        print(self.name + " is barking at " + dog.name)

    def has_bday(self):
        self.age += 1

def main():
    scooby = Dog("Scooby", "Great Dane", "Brown", 100, 100)

    print(scooby)
    scooby.bark()
    linus = Dog("linus", "pug", "black", 20, 10)
    linus.bark()
    linus.bark_at_dog(scooby)


main()
