def increment_password(pwd):
    pwd_list = list(pwd)
    i = len(pwd_list)-1
    while i >= 0:
        if pwd_list[i] == 'z':
            pwd_list[i] = 'a'
            i -= 1
        else:
            pwd_list[i] = chr(ord(pwd_list[i])+1)
            break
    return ''.join(pwd_list)

def increasing_three_straight_letters_check(pwd):
    pwd_list = list(pwd)
    ord_list = [ord(letter) for letter in pwd_list]
    i, checker = 0, 0
    while i < len(ord_list)-2:
        group_of_three = [ord_list[i], ord_list[i+1], ord_list[i+2]]
        if group_of_three[1] - group_of_three[0] == 1 and group_of_three[2] - group_of_three[1] == 1:
            checker += 1
            break
        i += 1
    if checker == 1:
        return True
    return False

def pair_check(pwd):
    pairs, i = [], 0
    while i < len(pwd)-1:
        cur_ele, next_ele = pwd[i], pwd[i+1]
        if cur_ele == next_ele:
            pairs.append(cur_ele*2)
            i += 2
            continue
        i += 1
    if len(set(pairs)) >= 2:
        return True
    return False

def iol_check(pwd):
    if 'i' not in pwd and 'o' not in pwd and 'l' not in pwd:
        return True
    return False


if __name__ == "__main__":
    cur_password = 'cqjxxyzz'  # Replace cur_password with cqjxxzaa to get answer for part 2
    while True:
        if iol_check(cur_password) and pair_check(cur_password) and increasing_three_straight_letters_check(cur_password):
            print(cur_password)
            break
        else:
            cur_password = increment_password(cur_password)