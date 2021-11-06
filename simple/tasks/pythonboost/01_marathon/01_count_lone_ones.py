def count_lone_ones_0(number: int) -> int:
    str_number = str(number)
    # q = [i for i in range(len(str_number) - 1) if str_number[i] = '1' and ]
    pass


from itertools import groupby


def count_lone_ones(number):
    # print([(i, list(j)) for i, j in groupby(str(number))])
    return sum(int(i) == len(list(j)) == 1 for i, j in groupby(str(number)))


print(count_lone_ones(101))
print(count_lone_ones(1191))
print(count_lone_ones(1111))
print(count_lone_ones(462))

# assert count_lone_ones(101) == 2
# assert count_lone_ones(1191) == 1
# assert count_lone_ones(1111) == 0
# assert count_lone_ones(462) == 0
