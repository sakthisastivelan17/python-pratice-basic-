class aircraft_engine:

    manufacturer='AeroTech'
    engine_count=0

    @classmethod
    def register_engine(cls):
        cls.engine_count+=1
        print('Engine count:',cls.engine_count)



aircraft_engine.register_engine()










    
 
    

