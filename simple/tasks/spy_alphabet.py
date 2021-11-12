from string import ascii_lowercase as alp

shift = 2
print(alp)


def decode_word(word):
    q = "".join(
        [
            alp[
                alp.index(_) + shift
                if alp.index(_) + shift <= len(alp)-1
                else alp.index(_) + shift - len(alp)
            ]
            for _ in word
        ]
    )
    return q


def uncode_word(word):
    q = "".join(
        [
            alp[
                alp.index(_) - shift
                if alp.index(_) - shift >= 0
                else alp.index(_) - shift + len(alp)
            ]
            for _ in word
        ]
    )
    return q


print(decode_word("python"))  # qzuipo
print(uncode_word("ravjqp"))  # python
