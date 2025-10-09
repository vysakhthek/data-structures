def generate_triangle(n):
    """
        input -> integer next
        output -> right angled triangle pattern of '*'
        
        each sides has n chars -> list of strings
        1 to n *s in each row
        
        psuedo code:
        
        iterater in list from 0 to n-1
            append '*'*i+1 times
    """
    
    triange_pattern = []
    for i in range(n):
        triange_pattern.append('*'*(i+1))
    return triange_pattern

if __name__ == "__main__":
    print(generate_triangle(5))