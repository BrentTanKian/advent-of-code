import re

def process_chars(line_string):
    total_string_length = len(line_string)
    remaining_string = line_string[1:-1]
    replace_hex = replace_hex_with_a(remaining_string)
    replace_slash_inverted_commas = replace_hex.replace(r'\"', '"')
    replace_double_slash = replace_slash_inverted_commas.replace(r"\\", "\\")
    return (total_string_length, len(replace_double_slash))

def replace_hex_with_a(s):
    return re.sub(r'\\x[0-9a-fA-F]{2}', 'a', s)

if __name__ == "__main__":
    file_path = 'input.txt'
    total_chars, in_memory_chars = 0, 0
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            processed_str = process_chars(line)
            total_chars += processed_str[0]
            in_memory_chars += processed_str[1]
    print(total_chars - in_memory_chars)





