class motor:
    def __init__(self,power,rpm):
        self.power=power
        self.rpm=rpm

    def display(self):
        print('motor power:',self.power)
        print('motor rpm:',self.rpm)


obj=motor(5000,7500)

obj.display()
