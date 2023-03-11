import unittest
from datetime import datetime
from ..car_factory import CarFactory

class Testcalliope(unittest.TestCase):
    def Test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year = today.year-3)
        current_mileage = 0
        last_service_mileage = 0
        
        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

if __name__ == "__main__":
    unittest.main()

