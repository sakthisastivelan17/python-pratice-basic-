file=open('vibration.txt','w')

file.write('12 \n')
file.write('18 \n')
file.write('15 \n')
file.write('20 \n')
file.write('25 \n')

file.close()

file=open('vibration.txt','r')

total=0
count=0
for line in file:
    changer=int(line)
    total=total+changer
    count=count+1

file.close()

print('average vibration:',total/count)





