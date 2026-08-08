snack_name = "Chips"
price = 3.50
quantity = 10
available = True

print("Today's snack is:", snack_name)
print("It costs", price)
print("you get:", quantity)
print("Is it available today:", available)

print(type(snack_name))
print(type(price))
print(type(quantity))
print(type(available))

total= price * quantity 
print("total value is", total)
print("Today's clearing value is:", total - 10)
print("Double stock:", quantity * 2)

print("Is the price under 5 Dollars?" , price<5)
print("Are there more than 10 in stock", quantity>=10)
print("Is price exactly 10.50?", price==10.50)

shopName= "Quick"+" "+"Bites"
print("Shop Name is:", shopName)
print("The numbers of letters in the snack name is",len(snack_name))
print("third letter of the snack name is:", snack_name[2])

a=3.50
b=4.50
print("Before : {a} and {b}")

temp=a
a=b
b=temp

print("After : {a} and {b}")

