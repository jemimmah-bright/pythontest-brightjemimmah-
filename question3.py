# Question 3(i)
#  Write a Python program that prompts a user to enter numbers. The process will repeat until
#  the user enters 0. Finally, the program prints sum of the numbers entered by the user.


def sum_numbers():
    total = 0
    while True:
        number = float(input("Enter a number (enter 0 to stop): "))
        if number == 0:
             total += number
             return total

result = sum_numbers()
print(f"The sum of the numbers entered is: {result}")





# Question 3(ii)
# Write a Python program to print all the numbers from 1 to 100 that are not divisible by 2
def print_odd_numbers():
    for number in range(1, 101):
        if number % 2 != 0: 
            print(number, end=" ")

print_odd_numbers()
