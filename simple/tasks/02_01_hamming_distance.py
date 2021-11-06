def hamming_distance(first_string: str, second_string: str) -> int:
    return sum(
        [1 for i in range(len(first_string)) if not first_string[i] == second_string[i]]
    )


# hamming_distance("abcde", "bcdef")
# hamming_distance("abcde", "abcde")
# hamming_distance("strong", "strung")
# hamming_distance("ABBA", "abba")

assert hamming_distance("abcde", "bcdef") == 5
assert hamming_distance("abcde", "abcde") == 0
assert hamming_distance("strong", "strung") == 1
assert hamming_distance("ABBA", "abba") == 4
