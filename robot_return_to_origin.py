moves = 'UDLL'
origin = [0,0]

def stringToInt(string):
    string_list = list(string)
    up_down_list = []
    left_right_list = []
    for char in string_list:
        if char == 'U' or 'D':
        up_down_list.append(char)
        else:
        left_right_list.append(char)
    print(up_down_list)

stringToInt("UDLL")