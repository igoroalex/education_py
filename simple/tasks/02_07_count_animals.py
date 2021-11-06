from collections import Counter


def count_animals(letters: str) -> int:

    animals = [
        "goat",
        "dog",
        "cat",
        "bat",
        "cock",
        "cow",
        "pig",
        "fox",
        "ant",
        "bird",
        "lion",
        "wolf",
        "deer",
        "bear",
        "frog",
        "hen",
        "mole",
        "duck",
    ]
    max_counter: int = 0
    animals_counters: list = [Counter(_) for _ in animals]

    def check_animal(letters_counter: Counter, count: int = 0):

        for animal in animals_counters:
            if animal == animal & letters_counter:
                check_animal(letters_counter - animal, count + 1)

        nonlocal max_counter
        max_counter = max(max_counter, count)

    check_animal(Counter(letters))
    return max_counter


# print(count_animals("cockdogwdufrbiraier"))
# print(count_animals("goatcode"))
# print(count_animals("cockdogwdufrbir"))
# print(count_animals("dogdogdogdogdog"))

assert count_animals("goatcode") == 2
assert count_animals("cockdogwdufrbir") == 4
assert count_animals("dogdogdogdogdog") == 5
