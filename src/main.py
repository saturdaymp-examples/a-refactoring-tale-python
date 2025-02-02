import sys

from .gilded_rose import *
from .repo import *

def main():
    print("OMGHAI!")
    items = get_items()

    days = 2
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1

    for day in range(days):
        print("-------- day %s --------" % day)
        print("name, sellIn, quality")
        for item in items:
            print(item)
        print("")
        GildedRose(items).update_quality()

if __name__ == "__main__":
    main()
