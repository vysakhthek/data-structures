

def generate_square(n: int) -> list:
    pattern = [0]*n
    for i in range(n):
        pattern[i] = '*' * n
    return pattern


pattern = generate_square(5)
print(pattern)