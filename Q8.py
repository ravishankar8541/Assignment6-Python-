"""Write a python script to check whether a given quadratic equation has two real &
distinct roots, real & equal roots or imaginary roots"""
print("Enter a,b and c :")
a,b,c=int(input()),int(input()),int(input())
D=b*b-4*a*c
if D>0:
 print("real and distinct roots")
elif D==0:
 print("real and equal roots")
else:
 print("imaginary roots")        

