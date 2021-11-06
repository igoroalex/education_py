def f(max_num, power):
    return list(filter(
        lambda x: sum(map(lambda y: pow(y, power), map(int, str(x)))) == x,
        range(2, max_num)
    ))


def fifth_powers():

    ans = [i for i in range(2, 1_000_000) if i == sum(int(_) ** 5 for _ in str(i))]
    ans = [i for i in range(2, 1_000_000) if i == sum(_ ** 5 for _ in map(int, str(i)))]
    print(ans)
    print(sum(ans))

def diff_powers_sum() -> int:
    max_num = 100
    sum_powers = sum(_ ** 2 for _ in range(1, max_num + 1))
    power_sum = sum(range(1, max_num + 1)) ** 2
    return abs(sum_powers - power_sum)
    
if __name__ == "__main__":
    # print(f_1(1000000, 5))
    # fifth_powers()
    # print(compute())
    # d = list(map(lambda x: x**5, range(2, 10)))
    # print(d)
    # print(diff_powers_sum())
    

