x = 300

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
num3 = int(input("Enter your third number: "))

def find_closest(a, b, c):
    x_a = abs(a - x)
    x_b = abs(b - x)
    x_c = abs(c - x)


    if x_a <= x_b and x_a <= x_c:
        return "A", a
    elif x_b <= x_a and x_b <= x_c:
        return "B", b
    else:
        return "C", c

letter, closest = find_closest(num1, num2, num3)
print(f"Letter{letter} or {closest} is the closest number to {x}")