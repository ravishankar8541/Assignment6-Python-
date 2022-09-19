#Write a python script to check whether a given year is a leap year or not.
year=int(input("Enter the any year :"))
if year%100==0:
    if year%400==0:
        print("Leap Year")
    else:
        print("Not Leap Year")   
elif year%4==0:
    print("Leap Year")
else:
    print("Not Leap Year")            