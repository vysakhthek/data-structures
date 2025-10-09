def generate_inverted_triangle(n):    
    """
        input -> int next
        output -> inverted right-angled triangle of pattern '*'
        each side n chars as ,list of strings
        fisrt row n stars
        n-1 start and so on
        
        
        pseuodo code:
            iterate from n to 
            append '*'* i 
            return list
    """
    inverted_traingle = []
    for i in range(n, 0, -1):
        inverted_traingle.append('*'*i)
    return inverted_traingle

if __name__ == "__main__":
    print(generate_inverted_triangle(5))