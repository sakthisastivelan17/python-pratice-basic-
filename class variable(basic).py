class phone:
    charger_type="C-type"
    def __init__(self,brand,cost,):
        self.brand=brand
        self.cost=cost

    def display(self):
        print('Brand:',self.brand)
        print('Cost:',self.cost)
        print('Charger Type:',self.charger_type)

phone.charger_type='B-type'       

samsung=phone('samsung M11 ',12000)
samsung.display()

realme=phone('realme c83',17000)
realme.display()

