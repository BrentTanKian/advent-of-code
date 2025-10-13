def look_and_say(string):
    new_str_list = []
    i, j = 0, 0
    while i < len(string) and j < len(string):
        cur = string[i]
        while j < len(string)-1 and string[j+1] == cur:
            j += 1
        length = j-i+1
        temp_str = str(length) + cur
        new_str_list.append(temp_str)
        i = j+1
        j = i
    new_str_gen = ''.join(new_str_list)
    return new_str_gen


if __name__ == "__main__":
    cur_str = '1321131112'
    counter = 0
    while counter != 40:  # Replace with 50 for part 2's answer
        cur_str = look_and_say(cur_str)
        counter += 1
    print(len(cur_str))







