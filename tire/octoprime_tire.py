from tire.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, tire_presure):
        self.tire_presure = tire_presure

    def needs_service(self):
        return sum(self.tire_presure) >= 3