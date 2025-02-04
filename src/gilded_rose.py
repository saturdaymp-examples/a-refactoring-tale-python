from ItemUpdator import update_item

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    # If ConjuredItem
    #   Do something
    # Else
    #   Do something

    def update_quality(self):
        for item in self.items:
            update_item(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
