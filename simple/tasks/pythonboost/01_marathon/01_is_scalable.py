def is_scalable(mount: list):
    # q = list(zip(mount, mount[1:]))
    return all(abs(a - b) <= 5 for a, b in zip(mount, mount[1:]))


print(is_scalable([1, 2, 4, 6, 7, 8]))
print(is_scalable([40, 45, 50, 45, 47, 52]))
print(is_scalable([2, 9, 11, 10, 18, 21]))

# assert is_scalable([1, 2, 4, 6, 7, 8]) == True
# assert is_scalable([40, 45, 50, 45, 47, 52]) == True
# assert is_scalable([2, 9, 11, 10, 18, 21]) == False
