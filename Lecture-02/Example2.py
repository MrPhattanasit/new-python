weight = int(input("Enter your Weight in kg: "))
height = float(input("Enter your Height in meters: "))
bmi = weight / (height ** 2)
print("Your BMI is:", format(bmi, ".2f"))