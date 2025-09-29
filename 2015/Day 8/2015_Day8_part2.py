def process_lengthen_chars(line_string):
    total_ori_len = len(line_string)
    encoded = '"' + line_string.replace('\\', '\\\\').replace('"', '\\"') + '"'
    return (total_ori_len, len(encoded))

if __name__ == "__main__":
    file_path = 'input.txt'
    total_chars, encoded_chars = 0, 0
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            processed_str = process_lengthen_chars(line)
            total_chars += processed_str[0]
            encoded_chars += processed_str[1]
    print(encoded_chars - total_chars)