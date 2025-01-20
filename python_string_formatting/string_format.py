txt = f"The price is 49 dollars"
print(txt)

#Example 2
price = 59
txt = f"The price is {price} dollars"
print(txt)

#Example 3
txt = f"The price is {95:.2f} dollars"
print(txt)

#Example 4
price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)

#Example 5
price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"

print(txt)

#Example 6
fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)

#Example 7
def myconverter(x):
  return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)

#Example 8
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

