import hashlib

def md5_hash_checker(input_string):
    start_num = 1
    while True:
        new_string = input_string + str(start_num)
        encoded_string = new_string.encode('utf-8')
        md5_object = hashlib.md5(encoded_string)
        md5_hash_value = md5_object.hexdigest()
        if md5_hash_value[:5] == "00000":
            break
        start_num += 1
    return start_num


if __name__ == "__main__":
    input_string = "ckczppom"
    int_value = md5_hash_checker(input_string)
    print(int_value)