def even(num):
    if num % 2 == 0:
        return True

nums = [1,2,3,4,5,6,7,8]
print(list(filter(even, nums)))


grater_than_five = list(filter(lambda x:x>5, nums))
print(grater_than_five)

even_and_grater_than_five = list(filter(lambda x:x%2==0 and x>5, nums))
print(even_and_grater_than_five)


persons = [
    {"name": "Vysakh", "age": 26},
    {"name": "Chikku", "age": 29},
    {"name": "carpe", "age": 20}
]

def age_grater_than(persons: list):
    return persons["age"] > 25

age_grater_than_25 = list(filter(age_grater_than, persons))
print(age_grater_than_25)