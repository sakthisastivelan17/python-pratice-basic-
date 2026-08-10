stress=float(input("enter stress :"))
fos=float (input("enter float:"))
if (stress >250):
    print( " design rejected ")
elif (stress==250 or fos>=2):
    print("design approved")
else:
    print("design need modification")
