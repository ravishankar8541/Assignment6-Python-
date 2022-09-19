""" Write a python script to print greater among three numbers. Print number only once
even if the numbers are the same."""

print("Enter three number :")
a,b,c=int(input()),int(input()),int(input())

print((a if a>c else c) if a>b else (b if b>c else c))