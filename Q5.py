# Write a python script to print two given words in dictionary order

print("Enter two words :")
a=input()
b=input()
print((b,a) if a>b else (a,b))