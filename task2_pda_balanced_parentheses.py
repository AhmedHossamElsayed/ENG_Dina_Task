def is_balanced_parentheses_and_anbn(string):
    stack = []
    inner_content = ""
    # Check for balanced parentheses
    for char in string:
        if char == '(':
            stack.append('(')
        elif char == ')':
            if not stack:
                return False
            stack.pop()
        else:
            inner_content += char  

    if stack:
        return False
    # Check for a's b's
    a_count = 0
    b_count = 0
    seen_b = False

    for char in inner_content:
        if char == 'a':
            if seen_b:
                return False
            a_count += 1
        elif char == 'b':
            seen_b = True
            b_count += 1
        else:
            return False  

    return a_count == b_count  

while True:
        print("1. Test a string")
        print("2. Exit")
        choice = input("Enter your choice (1 or 2): ")
        if choice == '2':
            print("Exiting...")
            break
        elif choice == '1':
            input_string = input("Enter a string: ")
            if is_balanced_parentheses_and_anbn(input_string):
                print("Accepted !! \n____________________\n")
            else:
                print("Rejected!! \n____________________\n")
        else:
            print("Invalid choice. Please enter 1 or 2.")   
