def sum_while(num: int) -> int:
    i = 1
    sum = 0
    while i < num:
        sum += i
        i += 1
    return sum

def sum_for(num: int) -> int:
    sum = 0
    for i in range(1, num):
        sum += i
    return sum

num = int(input("Enter the number"))
print("Result using While loop :", sum_while(num))
print("Reslut using For Loop :", sum_for(num))