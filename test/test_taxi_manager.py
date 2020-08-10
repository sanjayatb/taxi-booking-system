import unittest
from super_taxi.core.taxi_manager import taxi_manager,taxi_register
from super_taxi.model.taxis import Taxi


class TaxiRegisterTestCase(unittest.TestCase):
    def test_register_taxi(self):
        taxi_register.reset()
        self.assertEqual(1,taxi_register.register(Taxi()).id)
        self.assertEqual(2,taxi_register.register(Taxi()).id)
        self.assertEqual(3,taxi_register.register(Taxi()).id)

    def test_unregister_taxi(self):
        taxi_register.reset()
        taxi1 = taxi_register.register(Taxi())
        taxi_register.register(Taxi())
        taxi_register.unregister(taxi1)
        self.assertEqual(1,len(taxi_register.get_all_registered_taxis()))

    def test_registered_taxi_count(self):
        taxi_register.reset()
        taxi_register.register(Taxi())
        taxi_register.register(Taxi())
        self.assertEqual(2,taxi_register.registered_taxi_count())


class TaxiManagerTestCase(unittest.TestCase):
    def test_opt_in(self):
        taxi_manager.reset()
        taxi_manager.opt_in(Taxi())
        self.assertEqual(1,len(taxi_manager.get_active_taxis()))

    def test_opt_out(self):
        taxi_manager.reset()
        taxi1 = Taxi(1)
        taxi2 = Taxi(2)
        taxi_manager.opt_in(taxi1)
        taxi_manager.opt_in(taxi2)
        taxi_manager.opt_out(taxi1)
        self.assertEqual(1,len(taxi_manager.get_active_taxis()))


if __name__ == '__main__':
    unittest.main()
