import unittest
from shipping import delivery_fee


class DeliveryFeeTests(unittest.TestCase):
    def test_fifty_dollars_now_pays_fee(self):
        self.assertEqual(delivery_fee(5000), 500)

    def test_just_below_sixty_pays_fee(self):
        self.assertEqual(delivery_fee(5999), 500)

    def test_sixty_dollars_ships_free(self):
        self.assertEqual(delivery_fee(6000), 0)

    def test_above_sixty_ships_free(self):
        self.assertEqual(delivery_fee(7500), 0)

    def test_negative_order_is_rejected(self):
        with self.assertRaises(ValueError):
            delivery_fee(-1)


if __name__ == "__main__":
    unittest.main()
