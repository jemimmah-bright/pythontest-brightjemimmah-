# Question 1(i)
# Write a Python program to find the distance between two coordinate points (x1, y1) and (x2, y2).


# formula distance = math.sqrt[ (x2-x1)**2+ (y2-y1)**2]
# import math
# def distance(x1, y1, x2, y2):
#     import math
#     return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


# x1, y1 = 1, 2
# x2, y2 = 4, 6
# print(f"Distance between points ({x1}, {y1}) and ({x2}, {y2}) is: {distance(x1, y1, x2, y2):.2f}")









# Question 1(ii)
# Write a Python program to find maximum between three numbers.

def find_maximum(a, b, c):
    
    return max(a, b, c)


a, b, c = 2, 5, 15
print(f"The maximum between {a}, {b}, and {c} is: {find_maximum(a, b, c)}")





