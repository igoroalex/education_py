from string import ascii_letters


def gimme_the_letters(borders: str) -> str:
    x, y = borders.split(sep="-")
    return ascii_letters[ascii_letters.index(x): ascii_letters.index(y) + 1]


print(gimme_the_letters("a-z"))
print(gimme_the_letters("h-o"))
print(gimme_the_letters("Q-Z"))
print(gimme_the_letters("J-J"))
# assert gimme_the_letters("a-z") == "abcdefghijklmnopqrstuvwxyz"
# assert gimme_the_letters("h-o") == "hijklmno"
# assert gimme_the_letters("Q-Z") == "QRSTUVWXYZ"
# assert gimme_the_letters("J-J") == "J"
