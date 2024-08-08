from vehicle import Vehicle
#Car INHERITS from Vehicle
class Car(Vehicle):
# overwrite inherited go() method with one specific to car
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"