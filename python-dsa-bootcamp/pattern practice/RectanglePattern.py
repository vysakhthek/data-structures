

def generate_rectangle(n, m):
    """input -> 2ints
    output -> list of string (rectangular pattern of '*')
    n -> n0 of rows and m number of columns
    
    psuedo code:
        
        iterate in list n time append '*' * m times"""
        
    rectangle_pattern = []
    for i in range(n):
        rectangle_pattern.append('*'*m)
    return rectangle_pattern 


if __name__ == "__main__":
    print(generate_rectangle(4,5))