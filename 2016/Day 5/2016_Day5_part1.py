import hashlib

if __name__ == "__main__":
    door_id = 'ffykfhsq'
    cur_number, counter, password = 0, 0, ""
    while counter < 8:
        string = door_id + str(cur_number)
        hashed_result = hashlib.md5(string.encode()).hexdigest()
        if hashed_result[:5] == "00000":         
            password += hashed_result[5]
            counter += 1
        cur_number += 1
    print(password)
    
