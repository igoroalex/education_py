
def correct_sequence(s: str) -> bool:
    stack = []

    for i in s:
        if i in '[{(':
            stack.append(i)
        elif i in ']})':
            if not stack:
                print('incorrect')
                return False

            open_bracket = stack.pop()
            if open_bracket == '[' and i == ']':
                continue
            if open_bracket == '{' and i == '}':
                continue
            if open_bracket == '(' and i == ')':
                continue
            print('incorrect')
            return False
    if not stack:
        return True
    print('incorrect')
    return False


# bracket_sequence = input("your bracket's sequence")
bracket_sequence = '({})[]'
# bracket_sequence = '((())))'
# bracket_sequence = '({)]'

correct_sequence(bracket_sequence)
