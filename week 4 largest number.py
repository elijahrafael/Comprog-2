def find_largest(a,b,c):
    if a >= b and a >= c:
        return "A", a 
    elif b >= a and b >= c:
        return "B", b 
    else:
        return "C", c 

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
num3 = int(input("Enter your third number: "))

letter, largest = find_largest(num1, num2, num3)
print(f"Letter {letter} is the largest number with a value of {largest}")