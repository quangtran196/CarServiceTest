import unittest
from datetime import datetime

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire

#Test Batteries
class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        battery = SpindlerBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        battery = SpindlerBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        battery = NubbinBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        battery = NubbinBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())

#Test Engines
class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 92384
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        current_mileage = 4000
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())


class TestSternmanEngine(unittest.TestCase):
    def test_needs_service_true(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())

class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 45223
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        current_mileage = 10000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

#Test tire
class TestCarriganTire(unittest.TestCase):
    def test_needs_service_false(self):
        print()
        tire_ware = [0.4, 0.5, 0.2, 0.8]
        tire = CarriganTire(tire_ware)
        self.assertFalse(tire.needs_service())

    def test_needs_service_one_tire_true(self):
        tire_ware = [0.4, 0.9, 0.2, 0.8]
        tire = CarriganTire(tire_ware)
        self.assertTrue(tire.needs_service())
    
    def test_needs_service_two_tire_true(self):
        tire_ware = [0.4, 0.9, 0.94, 0.8]
        tire = CarriganTire(tire_ware)
        self.assertTrue(tire.needs_service())
    
    def test_needs_service_three_tire_true(self):
        tire_ware = [0.91, 0.92, 0.2, 0.98]
        tire = CarriganTire(tire_ware)
        self.assertTrue(tire.needs_service())
    
    def test_needs_service_all_tire_true(self):
        tire_ware = [0.94, 0.95, 0.92, 0.98]
        tire = CarriganTire(tire_ware)
        self.assertTrue(tire.needs_service())
    
class TestOctoprimeTire(unittest.TestCase):
    def test_needs_service_false(self):
        tire_ware = [0.4, 0.5, 0.2, 0.8]
        tire = OctoprimeTire(tire_ware)
        self.assertFalse(tire.needs_service())

    def test_needs_service_true(self):
        tire_ware = [1, 1, 1, 0.8]
        tire = OctoprimeTire(tire_ware)
        self.assertTrue(tire.needs_service())
    
if __name__ == '__main__':
    unittest.main()