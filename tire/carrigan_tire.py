from tire.tire import Tire

class CarriganTire(Tire):
    def __init__(self, tire_presure):
        self.tire_presure = tire_presure

    def needs_service(self):
        for num in self.tire_presure:
            if num >= 0.9:
                return True
        return False
