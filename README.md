# Something's Rotten at the Gilded Rose: A Python Refactoring Tale

Our tale begins at the Gilded Rose, a small inn with a prime location in a prominent city run by a friendly innkeeper named Allison. This quant inn sells a limited range of high-quality goods such as Aged Brie, Sulfuras, and concert tickets. Our unassuming hero developer has been hired to update the inn’s inventory system so Allison can sell conjured items. A simple task, or so it seems. Little does our hero know the perils and smells that await them in the rotten inventory source code.

Learn when and how to refactor in this hands-on presentation as we follow our hero through their refactoring journey of the famous Gilded Rose Kata. You can find a video of the presentation at:

https://youtu.be/CzHv3uY2KiU

Same refactoring using C#:

https://github.com/saturdaymp-examples/a-refactoring-tale-csharp

The original Gilded Rose Kata in many languages:

https://github.com/emilybache/GildedRose-Refactoring-Kata

# Gilded Rose starting position in Python

First off, read the [requirements](REQUIREMENTS.md).  Then either use the provided Docker environment or create your own.  This example should work on most version of Python 3.

This repo is the [Python](https://github.com/emilybache/GildedRose-Refactoring-Kata/tree/main/python) Gilded Rose Kata but will some changes to make it act more like a "real" Python application.

## Docker Environment

There is no Dockerfile, just a [docker-compose](docker-compose.yml) that use a Alpine Python image.  Run it:

```
docker compose run --rm app sh
```

You need to use `sh` instead of `bash` as it's a Alpine image.  Then you can run application:

```
python -m scr.main 5
```

This will output 5 days of item quality updates.  To run the tests:

```
python -m unittest
```

## Questions or Feedback?
If you have any questions or constructive feedback, please let me know by opening an [issue](https://github.com/saturdaymp-examples/a-refactoring-tale-python/issues) or reaching out to me via my contact information at [Saturday Morning Producitons](https://saturdaymp.com/).

Like this example?  Then please share it with others, star the repo, and/or [sponsor](https://github.com/sponsors/saturdaymp).

[![GitHub Sponsors](https://img.shields.io/github/sponsors/saturdaymp?label=Sponsors&logo=githubsponsors&labelColor=3C444C)](https://github.com/sponsors/saturdaymp)

## Acknowledgements
Thank you to [Dev Edmonton](https://devedmonton.com/) [JavaScript, Python, & Ruby Meetup](https://exchangejs.com/) for allowing me to present.  Also thank you, Terry Hughes, for creating the [Gilded Rose Kata](https://github.com/emilybache/GildedRose-Refactoring-Kata) and [Emily Bache](https://github.com/emilybache) for maintaining and expanding it.