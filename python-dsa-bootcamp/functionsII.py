import re

"""Function to return frequency of a character"""
def count_frequency(filepath: str) -> dict:
    char_count = {}
    with open(filepath, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower().strip('.,!?;:"\'')
                for char in word:
                    char_count[char] = char_count.get(char, 0) + 1

    return char_count

print(count_frequency('python-dsa-bootcamp\sample_text.txt'))


"""Function to validate email address"""
def is_valid_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.]+$'
    return re.match(pattern, email) is not None

print(is_valid_email("vysakh.thek@gmail.com"))
print(is_valid_email("1@gmail.com"))