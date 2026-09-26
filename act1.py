classmates=["aarav", "priya", "rahul", "sneha"]
print("class list :", classmates)

print("total students:" , len(classmates))
print("first student:", classmates[0])
print("last student:", classmates[-1]) 
print("first three student:", classmates[:3])

classmates.append("Meera")
print("After adding new student:", classmates)
classmates.remove("rahul")
print("After removing student:", classmates)
classmates.sort()
print("Sorted Alphabetically:", classmates)
classmates.reverse()
print("Reversed order:", classmates)

teacher = {"name" : "Mr. Sharma", "subject" : "python", "experience" : 5}
print("And Teacher profile:" , teacher)
print( "Subject", teacher["subject"])
print( "Experience ", teacher.get("experience", "not found"))
teacher["email"] = "sharma@school.com"
teacher["experience"] = 6
teacher.pop("experience")
print("Updated teacher profile:", teacher)

rollnumbers=[1,2,3,4,]
names = ["Aarav", "Priya", "Sneha"," Meera"]
studentdirectory = dict(zip(rollnumbers, names))
print("\student directory:" , studentdirectory)
print("\student  at roll 3:" , studentdirectory[3])
