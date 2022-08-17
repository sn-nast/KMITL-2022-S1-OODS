import math

h,w = [float(i) for i in input("Enter your High and Weight : ").split()]
bmi = w / (h**2)

if bmi >= 30 :
    print("Fat")
elif bmi >= 25 :
    print("Getting Fat")
elif bmi >= 23 :
    print("More than Normal Weight")
elif bmi >= 18.50 :
    print("Normal Weight")
else :
    print("Less Weight")