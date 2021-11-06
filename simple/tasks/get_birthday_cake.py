def get_birthday_cake(name: str, age: int) -> list:

    powder = "#" if age % 2 == 0 else "*"
    filling = f"{powder} {age} Happy Birthday {name}! {age} {powder}"
    cake = powder * len(filling)

    return [cake, filling, cake]


q = get_birthday_cake("John", 45)
[print(_) for _ in q]
