# User se integer input lena
number = int(input("Enter an integer: "))

# Table print karna
print(f"Table of {number}:")

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
