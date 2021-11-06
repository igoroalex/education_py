import string


def password_strength(password: str) -> str:
    digits = string.digits
    lowers = string.ascii_lowercase
    uppers = lowers.upper()
    if len(password) < 8:
        return 'Week'
    if all(a in digits for a in password):
        return 'Very week'
    return 'Good'


if __name__ == '__main__':
    assert password_strength('3refdf') == 'Week'
    assert password_strength('3rhetrhbfdrefdf') == 'Good'
    assert password_strength('123455768') == 'Very week'
    assert password_strength('3refdf') == 'Week'
    assert password_strength('3refdf') == 'Week'
    assert password_strength('3refdf') == 'Week'

# safety net
