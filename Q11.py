""" Write a python script to take the month value in numeric format and display the
number of days in it"""

month=int(input("Enter the month in numeric format :"))
if month in (1,3,5,7,8,10,12):
    print("31 days")
elif month in (4,6,9,11):
  print("30 days") 
elif month==2: 
    print("28 or 29 days")  
else:
    print("Invalid output")
 