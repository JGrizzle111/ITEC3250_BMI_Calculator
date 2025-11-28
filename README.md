# BMI Calculator

A comprehensive Body Mass Index (BMI) calculator written in Python that supports both standard (Imperial) and metric units with robust input validation and multiple output formats.

## 📋 Features

- **Dual Unit Support**: Calculate BMI using either standard units (pounds/inches) or metric units (kilograms/meters)
- **Input Validation**: Comprehensive error handling for invalid inputs and out-of-range values
- **Health Categories**: Automatic classification into standard health categories (Underweight, Normal weight, Overweight, Obese)
- **Flexible Output**: Choose from three different output formats to suit your needs
- **User-Friendly Interface**: Clear prompts and error messages for a smooth user experience

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system

### Installation

1. Clone this repository or download the `bmicalc.py` file
2. Navigate to the directory containing the file
3. Run the program using Python:

```bash
python bmicalc.py
```

## 📖 How to Use

1. **Select Unit Type**: Choose between standard units (1) or metric units (2)
2. **Enter Weight**: Input your weight within the specified range
3. **Enter Height**: Input your height within the specified range
4. **Choose Output Format**: Select how you want to see your results

### Input Ranges

#### Standard Units
- **Weight**: 20 - 700 pounds
- **Height**: 20 - 120 inches

#### Metric Units
- **Weight**: 10 - 300 kilograms
- **Height**: 0.5 - 3 meters

### Output Options

1. **BMI Value Only**: Displays your BMI rounded to two decimal places
2. **Health Category Only**: Shows your health classification
3. **Both**: Displays both BMI value and health category

## 🏥 BMI Categories

The calculator uses standard BMI ranges to classify results:

- **Underweight**: BMI < 18.5
- **Normal weight**: BMI 18.5 - 24.9
- **Overweight**: BMI 25.0 - 29.9
- **Obese**: BMI ≥ 30.0

## 💡 Example Usage

```
**************************
Body Mass Index Calculator
**************************
1. Standard Units
2. Metric Units
Please select your unit type: 1
**************************
Please enter your weight in pounds (20 - 700): 150
Please enter your height in inches (20 - 120): 68
**************************
Output Type
1: Display the BMI value only (rounded to two decimal places).
2: Display the health category only.
3. Display both the BMI value and the health category.
Please select your preferred output: 3
**************************
Your BMI is: 22.83 - You are classified as: Normal weight.
```

## ⚠️ Error Handling

The calculator includes robust error handling for:

- **Non-numeric input**: Prompts user to enter valid numbers
- **Out-of-range values**: Ensures inputs are within healthy/realistic ranges
- **Invalid menu selections**: Guides users to make valid choices
- **Recursive validation**: Continuously prompts until valid input is received

## 🔧 Technical Details

### BMI Calculation Formulas

- **Standard Units**: BMI = (weight in pounds / height in inches²) × 703
- **Metric Units**: BMI = weight in kilograms / height in meters²

### Code Structure

- `standardUnits()`: Handles Imperial unit calculations
- `metricUnits()`: Handles metric unit calculations
- `outputSelection()`: Manages result display and health categorization
- Global variable `bmi`: Stores calculated BMI value across functions

## 👥 Authors

- Joshua Grizzle
- Jacob Killingsworth
- Jeremy Luescher

**Course**: ITEC 3250 Section 01 - Assignment 6

## 📝 Notes

- The program uses integer input validation for simplicity
- For metric height input, consider that decimal values (like 1.75m) should be entered as whole numbers in this implementation
- All BMI categories follow standard medical guidelines

## 🤝 Contributing

This is a educational project for ITEC 3250. If you'd like to suggest improvements:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📜 License

This project is created for educational purposes as part of a university assignment.# ITEC3250_BMI_Calculator
