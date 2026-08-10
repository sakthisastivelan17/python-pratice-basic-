AL=float(input("enter applied load (k/n):"))
BC=float (input("enter beam capacity (k/n):"))
if(AL>BC):
    print("beam failurerisk ")
elif (AL==BC):
     print("at limit")
else :
    print("SAFE")
