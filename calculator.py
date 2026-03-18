x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

def a(x, y):
    return x + y
def s(x, y):    
    return x - y
def m(x,y) : 
    return  x * y
def d(x,y) :
    return x / y

print("1. Addition")   
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter choice (1/2/3/4): "))


    
    
    
if choice == 1:
        print(x, "+", y, "=", a(x, y))
elif choice == 2:
        print(x, "-", y, "=", s(x, y))
elif choice == 3:
        print(x, "*", y, "=", m(x, y))
elif choice == 4:
        print(x, "/", y, "=", d(x, y))
        if y == 0:
            print("Error: Division by zero is not allowed.")
else:
        print("Invalid input")
