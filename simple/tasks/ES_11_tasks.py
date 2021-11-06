def count_vowels(word: str) -> int:
    return sum([1 for _ in word if _ in "eyuioa"])


def is_full_house(hand: list) -> bool:
    return all([hand.count(_) >= 2 for _ in hand])


class IceCream:
    Plain = 0
    Vanilla = 5
    ChocolateChip = 5
    Strawberry = 10
    Chocolate = 10

    def __init__(self, flavor, sprinkles):
        self.flavor = flavor
        self.sprinkles = sprinkles


def sweetest_icecream(lst):
    sweety = {
        "Plain": 0,
        "Vanilla": 5,
        "ChocolateChip": 5,
        "Strawberry": 10,
        "Chocolate": 10,
    }
    return max([sweety[ice.flavor] + ice.sprinkles for ice in lst])


# реализовать эту функцию
if __name__ == "__main__":
    ice1 = IceCream("Chocolate", 13)
    ice2 = IceCream("Vanilla", 0)
    ice3 = IceCream("Strawberry", 7)
    print(sweetest_icecream([ice1, ice2, ice3]))