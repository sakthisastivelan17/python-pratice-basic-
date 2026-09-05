class laptop :
    name = ''
    price = ''
    processor = ''
    ram = ''

hp = laptop()
dell = laptop()
lenovo = laptop()

hp.name = 'hp'
dell.name = 'dell'
lenovo.name = 'lenovo'

hp.price = 65890
dell.price = 70000
lenovo.price = 45000

hp.processor = 'intel i7 core'
dell.processor = 'intel i5 '
lenovo.processor = 'intel i11'

hp.ram = '32gb'
dell.ram = '8gb'
lenovo.ram = '16gb'

print('1)',hp.name)
print('price:',hp.price)
print('processor:',hp.processor)
print('ram:',hp.ram)
print()
print('1)',dell.name)
print('price:',dell.price)
print('processor:',dell.processor)
print('ram:',dell.ram)
print()
print('1)',lenovo.name)
print('price:',lenovo.price)
print('processor:',lenovo.processor)
print('ram:',lenovo.ram)
