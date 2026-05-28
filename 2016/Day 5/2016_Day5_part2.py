import hashlib

if __name__ == "__main__":
    door_id = 'ffykfhsq'
    cur_number, password_list, positions = 0, [" ", " ", " ", " ", " ", " ", " ", " "], set()
    while " " in password_list:
        string = door_id + str(cur_number)
        hashed_result = hashlib.md5(string.encode()).hexdigest()
        if hashed_result[:5] == "00000" and hashed_result[5].isdigit() and int(hashed_result[5]) <= 7 and int(hashed_result[5]) not in positions:
            password_list[int(hashed_result[5])] = hashed_result[6]
            positions.add(int(hashed_result[5]))
        cur_number += 1
    print(''.join(password_list))