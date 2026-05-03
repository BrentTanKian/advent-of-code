def string_process(room):
    string_copy1, string_copy2, string_copy3 = room, room, room
    string_list1 = string_copy1.split('[')
    answer = string_list1[-1][:-1]
    string_list2 = string_copy2.split('-')
    dirty_checksum = string_list2[-1]
    checksum = int(dirty_checksum.replace('['+answer+']',''))
    room_name = ''.join(string_copy3.split('-')[:-1])
    return [room_name, checksum, answer]


def find_answer(room):
    string_dict = {}
    for letter in room:
        if letter not in string_dict:
            string_dict[letter] = 1
        else:
            string_dict[letter] += 1
    tuple_list = list(string_dict.items())
    tuple_list.sort(key=lambda x: x[0])
    tuple_list.sort(key=lambda x: x[1], reverse=True)
    found_answer_list = tuple_list[:5]
    found_answer_str = ''.join([group[0] for group in found_answer_list])
    return found_answer_str


if __name__ == "__main__":
    total = 0
    with open("input.txt", "r") as file:
        content = file.readlines()
    cleaned_lines = [line.strip() for line in content]
    for line in cleaned_lines:
        results = string_process(line)
        found_answer = find_answer(results[0])
        if found_answer == results[2]:
            total += results[1]
    print(total)
