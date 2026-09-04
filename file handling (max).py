file=open('pressure.txt','w')

file.write('120 \n')
file.write('250 \n')
file.write('180 \n')
file.write('320 \n')
file.write('275 \n')

file.close()

file=open('pressure.txt','r')

max_pressure=[]

for line in file:
    changer=int(line)
    max_pressure.append(changer)

file.close()

maxer=max(max_pressure)
print('maxium pressure:',maxer)


