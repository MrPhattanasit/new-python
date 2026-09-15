def divide(a, b):
    try:
        result = a / b 
    except ZeroDivisionError:
        print("Error Division by zero is not allowed.")
        return None
    else:
        return result
a,b = map(int, input("Enter two numbers separated by space: ").split())
print(f"the result of {a} divided by {b} is: {divide(a, b)}")
print("End of program.")