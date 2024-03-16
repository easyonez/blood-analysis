from array import *
import tkinter as tk

blood_test_items = [
    "Complete Blood Count (CBC)",
    "Blood Glucose",
    "Cholesterol Levels",
    "Liver Function Tests",
    "Kidney Function Tests",
    "Thyroid Function Tests",
    "Electrolyte Levels",
    "Iron Levels",
    "Vitamin Levels",
    "Hormone Levels",
    # Add more items as needed
]

def test():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    fasting = input("Are you fasting? (y/n): ")
    if fasting == "y":
        fasting = True
    elif fasting == "n":
        fasting = False
    else:
        print("Invalid input")
        return


if __name__ == "__main__":
    test()
    # pass