
low_num, up_num = 2, 100
row = set(a ** b for a in range(low_num, up_num + 1) for b in range(low_num, up_num + 1))

print(len(row))
