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


even_or_odd = lambda num:num%2 ==0
print(even_or_odd(6))


nums = [1,2,3,4,5,6,7]

squared = map(lambda num:num**2, nums)
print(list(squared))


nums2 = [1,2,3,4]
nums1 = [4,5,6,7]

added_nums = list(map(lambda num1,num2:num1+num2, nums1, nums2))
print(added_nums)

str_nums = ['1','2','3','4','5']
int_nums = list(map(int, str_nums))

print(int_nums)

str_letters = ['a','b','c','d','e']
upper_letters = list(map(str.upper, str_letters))

print(upper_letters)


def get_name(persons):
    return persons['name']

persons = [
    {'name': 'vysakh'},
    {'name': 'carpe'}
]

names = list(map(get_name, persons))
print(names)