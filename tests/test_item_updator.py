import unittest

from gilded_rose import Item
from src.item_updator import update_item

class GildedRoseTest(unittest.TestCase):
    def test_update_normal_item_before_sell_date(self):
        item = Item("normal item", 1, 10)
        update_item(item)

        self.assertEqual(item.quality, 9)
        self.assertEqual(item.sell_in, 0)

    def test_update_normal_item_after_sell_date(self):
        item = Item("normal item", 0, 10)
        update_item(item)

        self.assertEqual(item.quality, 8)
        self.assertEqual(item.sell_in, -1)

    def test_update_conjured_item_before_sell_date(self):
        item = Item("Conjured Item", 1, 10)
        update_item(item)

        self.assertEqual(item.quality, 8)
        self.assertEqual(item.sell_in, 0)

    def test_update_conjured_item_after_sell_date(self):
        item = Item("Conjured Item", 0, 10)
        update_item(item)

        self.assertEqual(item.quality, 6)
        self.assertEqual(item.sell_in, -1)

if __name__ == '__main__':
    unittest.main()
