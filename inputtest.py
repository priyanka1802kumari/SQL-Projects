#Q1
name = input("your name ?")
print("hello",name)

#Q2

first_name = input(" your first name")
surname =input("your surname")

print("hello",first_name, surname)
#Q4
print("what do you call a bear with no teeth?\nagummy bear")
#Q4
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

total = num1 + num2
print("The total is", total)
#Q5
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

answer = (num1 + num2) * num3
print("The answer is", answer)

#Q6
start = int(input("How many slices of pizza did you start with? "))
eaten = int(input("How many slices did you eat? "))

left = start - eaten
print("You have", left, "slices left.")

#Q7
name = input("Enter your name: ")
age = int(input("Enter your age: "))

new_age = age + 1
print(name, "next birthday you will be", new_age)

#Q8
bill = float(input("Enter total bill amount: "))
diners = int(input("Enter number of diners: "))

each_person = bill / diners
print("Each person must pay", each_person)

#Q9
days = int(input("Enter number of days: "))

hours = days * 24
minutes = days * 24 * 60
seconds = days * 24 * 60 * 60

print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)

#Q10
kg = float(input("Enter weight in kilograms: "))

pounds = kg * 2.204
print("Weight in pounds is", pounds)

#Q11
large = int(input("Enter a number over 100: "))
small = int(input("Enter a number under 10: "))

times = large // small

print(small, "goes into", large, times, "times.")


number =int(input("enter a first number:"))
answer =(number**2) + (number**3)
print("answer is", answer)