from string import ascii_uppercase


def diamond(letter: str, background: str = ' ') -> str:
    length = ascii_uppercase.index(letter)
    template = [[background for __ in range(length * 2 + 1)] for _ in range(length + 1)]
    template[0][length] = 'A'
    for index in range(1, len(template)):
        template[index][length - index] = ascii_uppercase[index]
        template[index][-(length - index) - 1] = ascii_uppercase[index]
    template.extend(list(reversed(template))[1:])
    return '\n'.join(''.join(_) for _ in template) + '\n'


print(diamond('D'))
