def string_process(room):
    string_copy1, string_copy2, string_copy3 = room, room, room
    string_list1 = string_copy1.split('[')
    answer = string_list1[-1][:-1]
    string_list2 = string_copy2.split('-')
    dirty_checksum = string_list2[-1]
    checksum = int(dirty_checksum.replace('['+answer+']',''))
    room_name = ''.join(string_copy3.split('-')[:-1])
    return [room_name, checksum, answer]


def cipher_transform(room, checksum):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_str = ''
    for letter in room:
        start = 0
        letter_index = alphabet.index(letter)
        while start < checksum:
            letter_index += 1
            if letter_index > 25:
                letter_index = 0
            start += 1
        new_str += alphabet[letter_index]
    return new_str


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        content = file.readlines()
    cleaned_lines = [line.strip() for line in content]
    for line in cleaned_lines:
        results = string_process(line)
        new_string = cipher_transform(results[0], results[1])
        if new_string == 'northpoleobjectstorage':
            print(results[1])
            break