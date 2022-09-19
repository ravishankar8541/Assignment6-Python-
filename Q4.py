"""Write a python script to print greater between two numbers. Print number only once
even if the numbers are the same."""

a=int(input("Enter a first number :"))
b=int(input("Enter a second number:"))

print(a if a>b else b)