
def same_length(binary_sequence: int) -> bool:
    """find out if binary sequence is correct closed"""
    binary_sequence = str(binary_sequence)
    while "10" in binary_sequence:
        binary_sequence = binary_sequence.replace("10", "")
    return len(binary_sequence) == 0
    # return not binary_sequence #  больше нравиться верняя строка, но так тоже работает, подскажите


# assert same_length(110011100010) == True
# assert same_length(101010110) == False
# assert same_length(111100001100) == True
# assert same_length(111) == False
