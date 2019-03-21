def stringToInt(string):
    string_list = list(string)
    up  = []
    down = []
    left = []
    right = []
    for char in string_list:
        if char == 'U':
            up.append(char)
        elif char == 'D':
            down.append(char)
        elif char == 'R':
            right.append(char)
        elif char == 'L':
            left.append(char)
    if  len(up) == len(down) and len(right) == len(left):
        return True
    else:
        return False

    print(up, down, left, right)

stringToInt("UDLL")