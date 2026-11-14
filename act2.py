class student:
    age = 12
    name = "Bob"

    def introduction(self):
        print("Hi I am a student")

    def details(self):
        print("My name is", self.name)
        print("I am", self.age)

ob = student()
ob.introduction()
ob.details()