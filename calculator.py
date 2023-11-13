import math

def add(x, y):
    return x +  y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def square_root(x):
    if x < 0:
        return "Error: Square root of a negative  number"
    return math.sqrt(x)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def main():
    while True:
        print("Scientific Calculator Menu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Square Root")
        print("6. Sine")
        print("7. Cosine")
        print("8. Tangent")
        print("9. Exit")

        choice = input(" ")

        if choice == '9':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

        elif choice == '5':
            num1 = float(input("Enter a number: "))

        elif choice in ('6', '7', '8'):
            angle = float(input("Enter an angle in degrees: "))

        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)
        elif choice == '5':
            result = square_root(num1)
        elif choice == '6':
            result = sin(angle)
        elif choice == '7':
            result = cos(angle)
        elif choice == '8':
            result = tan(angle)
        
        print("Result:", result)

if __name__ == "__main__":
    main()
