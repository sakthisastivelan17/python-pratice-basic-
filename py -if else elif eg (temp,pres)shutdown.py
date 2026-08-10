temperature=float(input("enter temperature:"))
pressure=float(input("enter pressure:"))
if (temperature>100 or pressure>20):
    print("EMERGENGY SHUTDOWN")
elif(temperature>80 or pressure>15):
    print("WARNING!!! INSPECT COMPRESSOR")
else:
     print ("NORMAL OPERATION")
