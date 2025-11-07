# BMI Health Analyzer

def bmi_analyzer():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return  # Exit the function if input is invalid

    if height <= 0 or weight <= 0:
        print("Height and weight must be positive numbers.")
        return

    # BMI calculation
    bmi = weight / (height ** 2)
    print(f"Your BMI is: {bmi:.2f}")

    # BMI classification
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi <= 24.9:
        category = "Normal weight"
    elif 25 <= bmi <= 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    print(f"Health category: {category}")

# Call the function
bmi_analyzer()
