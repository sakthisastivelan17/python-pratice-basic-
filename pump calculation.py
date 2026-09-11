class pump:
    def __init__(self,flow_rate,pressure):
        self.flow_rate=flow_rate
        self.pressure=pressure

    def power(self):
        Q=self.flow_rate
        deltaP=self.pressure
        p=Q*deltaP
        p1=p/1000
        print('Pump Power(in Watts):',p,'W')
        print('pump power(in Kilowatts):',p1,'Kw')

obj=pump(0.05,200000)

obj.power()




