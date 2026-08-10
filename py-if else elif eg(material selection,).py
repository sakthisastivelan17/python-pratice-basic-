temperature=float(input("enter temperature for material selection: "))
if (temperature>500):
    print("use superalloy")
elif(temperature>200):
    print ("use stainless steeel")
else:
     print("use mild steel")
