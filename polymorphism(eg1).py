# polymorphism : 

# here sound is one method but it has many different forms ,so that is polymorphism .


class animal:
    def sound(self):
        print("Animal makes sound")

class dog():
    def sound(self):
        print("Dog barks")

class cat():
    def sound(self):
        print("Cat meows")

a1 = animal()
d1 = dog()
c1 = cat()

a1.sound()
d1.sound()
c1.sound()
        

