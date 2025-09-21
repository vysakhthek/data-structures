
def ticketPrice(age: int, is_student: str) -> str:

    if age > 0:
        if age < 18:
            price = "$5"
        elif age >=18 and age < 60:    
            if is_student == "yes":
                price = "$5"
            else:
                price = "$20"

        elif age > 60:
            if is_student == "yes":
                price = "$5"
            else:
                price = "$10"
    else:
        price = "Not a Valid Age"

    return price

age = int(input("Enter the age"))
is_student = str(input("Are you a student? Yes / No"))

price = ticketPrice(age, is_student)
print("Ticket Price :", price)