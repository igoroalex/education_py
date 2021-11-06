def join_digits(n: int) -> str:
    # return "-".join("".join(map(str, range(1, n + 1))))
    return "-".join("".join([str(i) for i in range(1, n + 1)]))


print(join_digits(15))
