def is_pandigital(number: int) -> bool:
    """get whether a number is pan digital"""
    return len(set(str(number))) == 10


# assert is_pandigital(98140723568910) == True
# assert is_pandigital(90864523148909) == False
# assert is_pandigital(112233445566778899) == False
