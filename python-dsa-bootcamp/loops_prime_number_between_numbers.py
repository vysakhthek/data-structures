from typing import List

def primeBetweeen(start: int, end: int) -> List[int]:
    prime_output = []
    for num in range(start, end+1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                prime_output.append(num)
    return prime_output

start = int(input("Enter the Start Number"))
end = int(input("Enter the End Number"))

prime_output = primeBetweeen(start, end)
print(f"Prime Numbers between {start} and {end} are : {prime_output}")