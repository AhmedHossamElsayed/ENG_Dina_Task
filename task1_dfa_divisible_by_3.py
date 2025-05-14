def dfa_divisible_by_3(binary_string):
    state = 0

    for bit in binary_string:
        if bit not in {'0', '1'}:
            return False  
        if state == 0:
            state = 0 if bit == '0' else 1
        elif state == 1:
            state = 2 if bit == '1' else 1
        elif state == 2:
            state = 0 if bit == '1' else 2

    # Accept if the final state is 0
    return state == 0

binary_string = input("Enter a binary string: ")
if dfa_divisible_by_3(binary_string):
    print("Accepted: The number of 1s is divisible by 3.")
else:
    print("Rejected: The number of 1s is not divisible by 3.")