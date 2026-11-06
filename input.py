# name = "Abhi"

# input(prompt)
# prompt is visible to the user. 
# Based on that prompt, he can input the values.

# name = input("What is your name? ")

# print("Hello ",name)

# x = input("Enter a number:")
# y = input("Enter another number:")

# print(type(x), type(y))

# print(x+y)

# By default, any value passed through the input function
# is of str type.

# Type casting -> Changing the nature of the value
# str()
# int()
# float()
# x = int(input("Enter a number to be squared: "))

# print(x**2)

# y = "45"
# print(int(y))
# print(float(y))

# print(str(676))

# We have to take principal, rate and time from user.
# We have to calculate the simple interest.

principal = int (input("what is the principal value ?"))
rate = float(input("what is the rate value?"))
time = int(input("what is the time value?"))

simple_interest = (principal*rate*time)/100
print(simple_interest)