def update(item):
    if is_conjured_item(item):
        update_conjured(item)
    else:
        update_normal_brie_sulfuras_baskstage(item)

def is_conjured_item(item):
    return item.name.startswith("Conjured")

def update_normal_brie_sulfuras_baskstage(item):
    if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
        if item.quality > 0:
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.quality = item.quality - 1
    else:
        if item.quality < 50:
            item.quality = item.quality + 1
            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.sell_in < 11:
                    if item.quality < 50:
                        item.quality = item.quality + 1
                if item.sell_in < 6:
                    if item.quality < 50:
                        item.quality = item.quality + 1
    if item.name != "Sulfuras, Hand of Ragnaros":
        item.sell_in = item.sell_in - 1
    if item.sell_in < 0:
        if item.name != "Aged Brie":
            if item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                item.quality = item.quality - item.quality
        else:
            if item.quality < 50:
                item.quality = item.quality + 1


def update_conjured(item):
    if item.sell_in > 0:
        item.quality -= 2
    else:
        item.quality -= 4

    if item.quality < 0:
        item.quality = 0

    item.sell_in = item.sell_in - 1