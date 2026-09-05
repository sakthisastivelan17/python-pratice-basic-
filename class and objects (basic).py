class goa :
    name=''
    drink=''
    swim=''

    def party(self):
        print('lets party !!')
    def beach(self):
        print('lets go to beach')

ramesh = goa()
suresh = goa()

ramesh.name = 'Ramesh kuttan'
suresh.name = 'suresh chettan'

ramesh.drink = 'Yes'
suresh.drink = 'No'

ramesh.swim = 'no'
suresh.swim = 'yes'

print(ramesh.name)
print(suresh.name)

print(ramesh.drink)
print(suresh.drink)

print(ramesh.swim)
print(suresh.swim)
