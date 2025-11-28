"""
BMI Calculator
ITEC 3250 Section 01 - Assignment 6
Authors: Joshua Grizzle, Jacob Killingsworth, Jeremy Luescher

A comprehensive Body Mass Index calculator that supports both standard (Imperial) 
and metric units with input validation and multiple output formats.
"""

# Display welcome message and unit selection menu
print("**************************")
print("Body Mass Index Calculator")
print("**************************")
print("1. Standard Units")
print("2. Metric Units")
unitType = int(input("Please select your unit type: "))
print("**************************")

# Global variable to store the calculated BMI value
bmi = 0

def standardUnits():
    """
    Handles BMI calculation using standard (Imperial) units.
    Prompts user for weight in pounds and height in inches.
    Includes input validation with appropriate error handling.
    """
    # Get weight input with validation for reasonable range
    weight = input("Please enter your weight in pounds (20 - 700): ")
    try:
        # Convert string input to integer for calculation
        num = int(weight)
        # Validate weight is within acceptable range
        if 20 <= num <= 700:
            # Get height input after successful weight validation
            height = input("Please enter your height in inches (20 - 120): ")
            try: 
                # Convert height string to integer
                height_num = int(height)
                # Validate height is within reasonable range
                if 20 <= height_num <= 120:
                    # Calculate BMI using standard formula: (weight/height²) × 703
                    global bmi
                    bmi = (num/(height_num * height_num)) * 703
                else:
                    # Height out of range - prompt user to try again
                    print("Input out of range: Please enter 20 - 120.")
                    standardUnits()
            except ValueError:
                # Handle non-numeric height input
                print("Invalid input: Please enter a number.")
                standardUnits() 
        else:
            # Weight out of range - prompt user to try again
            print("Input out of range: Please enter 20 - 700.")
            standardUnits()
    except ValueError:
        # Handle non-numeric weight input
        print("Invalid input: Please enter a number.")
        standardUnits()

def metricUnits():
    """
    Handles BMI calculation using metric units.
    Prompts user for weight in kilograms and height in meters.
    Includes input validation with appropriate error handling.
    """
    # Get weight input with validation for reasonable range
    weight = input("Please enter your weight in kilograms (10 - 300): ")
    try:
        # Convert string input to integer for calculation
        num = int(weight)
        # Validate weight is within acceptable range
        if 10 <= num <= 300:
            # Get height input after successful weight validation
            height = input("Please enter your height in meters (0.5 - 3): ")
            try: 
                # Convert height string to integer (Note: should be float for meters)
                height_num = int(height)
                # Validate height is within reasonable range
                if  0.5 <= height_num <= 3:
                    # Calculate BMI using metric formula: weight/height²
                    global bmi
                    bmi = num/(height_num * height_num)
                else:
                    # Height out of range - prompt user to try again
                    print("Input out of range: Please enter 0.5 - 3.")
                    metricUnits()
            except ValueError:
                # Handle non-numeric height input
                print("Invalid input: Please enter a number.")
                metricUnits() 
        else:
            # Weight out of range - prompt user to try again
            print("Input out of range: Please enter 10 - 300.")
            metricUnits()
    except ValueError:
        # Handle non-numeric weight input
        print("Invalid input: Please enter a number.")
        metricUnits()

def outputSelection():
    """
    Handles the output format selection and displays results.
    Categorizes BMI into health categories and provides multiple output options.
    Includes input validation with recursive error handling.
    """
    global bmi
    
    # Determine health category based on standard BMI ranges
    if bmi < 18.5:
        healthCategory = "Underweight"
    elif 18.5 <= bmi <= 24.9:
        healthCategory = "Normal weight"
    elif 25 <= bmi <= 29.9:
        healthCategory = "Overweight"
    else:
        healthCategory = "Obese"

    # Display output format options to user
    print("**************************")
    print("Output Type")
    print("1: Display the BMI value only (rounded to two decimal places).")
    print("2: Display the health category only.")
    print("3. Display both the BMI value and the health category.")
    outputType = input("Please select your preferred output: ")
    print("**************************")
    
    try:
        # Convert user input to integer for comparison
        outputType_num = int(outputType)
        # Display results based on user's choice
        if outputType_num == 1:
            # Show only BMI value rounded to 2 decimal places
            print(f"Your BMI is: {bmi:.2f}")
        elif outputType_num == 2:
            # Show only health category classification
            print(f"You are classified as: {healthCategory}.")
        elif outputType_num == 3:
            # Show both BMI value and health category
            print(f"Your BMI is: {bmi:.2f} - You are classified as: {healthCategory}.")
        else:
            # Invalid choice - prompt user to try again
            print("Invalid choice: Please select 1, 2, or 3.")
            outputSelection()
    except ValueError:
        # Handle non-numeric input
        print("Invalid input: Please enter a number.")
        outputSelection()

# Main program execution based on user's unit type selection
if unitType == 1:
    # User selected standard units (pounds and inches)
    standardUnits()
    outputSelection()
elif unitType == 2:
    # User selected metric units (kilograms and meters)
    metricUnits()
    outputSelection()
else:
    # Invalid unit type selection
    print("Invalid choice: Please select Standard Units or Metric Units")
