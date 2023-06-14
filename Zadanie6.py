class Dog:
    count = 0  # this is a class variable
    dogs = []  # this is a class variable

    def __init__(self, name):
        self.name = name  # self.name is an instance variable
        Dog.count += 1
        Dog.dogs.append(name)

    def bark(self, n):  # this is an instance method
        print("{} says: {}".format(self.name, "woof! " * n))

    @staticmethod
    def dog_info():
        print(f"Number of dogs: {Dog.count}")
        print("Dog names are: ")
        for name in Dog.dogs:
            print(name)


dog1 = Dog("Lake")
dog2 = Dog("Jasy")

dog1.bark(3)
dog2.bark(2)

Dog.dog_info()
