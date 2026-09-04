file=open('tools.txt','w')
file.write('Spanner\n')
file.write('Wrench\n')
file.write('Hammer\n')
file.write('Screwdriver\n')
file.write('Allen Key\n')
file.close()

file=open('tools.txt','r')
a=input('enter the tool to found exists:')

data=file.read()

if a in data:
    print('tool found')
    
else:
    print('tool not found')

file.close()
