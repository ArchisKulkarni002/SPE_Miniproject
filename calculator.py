import math

def log(message):
    print("INFO: ", message)

def error(message):
    print("ERROR: ", message)

def calculateSquareRoot(x):
    return math.sqrt(x)

def calculateFactorial(x):
    return math.factorial(x)

def calculateNaturalLog(x):
    return math.log(x)

def calculatePower(base, exponent):
    return math.pow(base, exponent)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def scientificMenu():
    while True:
        print("\nScientific Operations")
        print("1. Square Root (√x)")
        print("2. Factorial (x!)")
        print("3. Natural Logarithm (ln x)")
        print("4. Power Function (xʸ)")
        print("5. Back to Main Menu")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            x = float(input("Enter a number: "))
            if x < 0:
                error("Square root of a negative number is not defined.")
            else:
                log(f"Result: √{x} = {calculateSquareRoot(x)}")
        
        elif choice == '2':
            x = int(input("Enter a number: "))
            if x < 0:
                error("Error: Factorial of a negative number is not defined.")
            else:
                log(f"Result: {x}! = {calculateFactorial(x)}")
        
        elif choice == '3':
            x = float(input("Enter a number: "))
            if x <= 0:
                error("Error: Natural logarithm is only defined for positive numbers.")
            else:
                log(f"Result: ln({x}) = {calculateNaturalLog(x)}")
        
        elif choice == '4':
            base = float(input("Enter base: "))
            exponent = float(input("Enter exponent: "))
            log(f"Result: {base}^{exponent} = {calculatePower(base, exponent)}")
        
        elif choice == '5':
            break
        else:
            error("Invalid choice. Please select a valid option.")

def main():
    while True:
        print("\nCalculator Menu")
        print("1. Basic Operations")
        print("2. Scientific Operations")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ")
        
        if choice == '1':
            while True:
                print("\nBasic Operations")
                print("1. Addition (+)")
                print("2. Subtraction (-)")
                print("3. Multiplication (*)")
                print("4. Division (/)")
                print("5. Back to Main Menu")
                
                basicChoice = input("Choose an option (1-5): ")
                
                if basicChoice == '1':
                    x = float(input("Enter first number: "))
                    y = float(input("Enter second number: "))
                    log(f"Result: {x} + {y} = {add(x, y)}")
                
                elif basicChoice == '2':
                    x = float(input("Enter first number: "))
                    y = float(input("Enter second number: "))
                    log(f"Result: {x} - {y} = {subtract(x, y)}")
                
                elif basicChoice == '3':
                    x = float(input("Enter first number: "))
                    y = float(input("Enter second number: "))
                    log(f"Result: {x} * {y} = {multiply(x, y)}")
                
                elif basicChoice == '4':
                    x = float(input("Enter first number: "))
                    y = float(input("Enter second number: "))
                    log(f"Result: {x} / {y} = {divide(x, y)}")
                
                elif basicChoice == '5':
                    break
                else:
                    error("Invalid choice. Please select a valid option.")
        
        elif choice == '2':
            scientificMenu()
        
        elif choice == '3':
            log("Exiting calculator. Goodbye!")
            break
        
        else:
            error("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
