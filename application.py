from array import *
import tkinter as tk
    
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
    # Add more items as neded
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
    
    info = [name, age, fasting]
    
    print ("Name: " + name + "\nAge: " + str(age) + "\nFasting: " + str(fasting))
    return

import tkinter as tk

class MainView:
    def __init__(self, root):
        self.root = root
        self.root.title("Blood Analysis")
        
        # Create and configure the main frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=20, pady=20)
        
        # Create and configure the widgets
        self.label = tk.Label(self.main_frame, text="Welcome to Blood Analysis!")
        self.label.pack(pady=10)
        self.__version = tk.Label(self.main_frame, text="1.0.1")
        self.__version.pack(pady=10)
        
        self.button = tk.Button(self.main_frame, text="Click Me", command=self.button_clicked)
        self.button.pack(pady=10)
        
    def button_clicked(self):
        self.button.destroy()
        self.root.geometry("500x200")
        self.label.config(text="Please enter your information")

        self.name_label = tk.Label(self.main_frame, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.main_frame)
        self.name_entry.pack()
        print(self.name_entry.get())

        self.age_label = tk.Label(self.main_frame, text="Age:")
        self.age_label.pack()
        self.age_entry = tk.Entry(self.main_frame)
        self.age_entry.pack()
        print(self.age_entry.get())

        self.fasting_label = tk.Label(self.main_frame, text="Fasting? (y/n):")
        self.fasting_label.pack()
        self.fasting_entry = tk.Entry(self.main_frame)
        self.fasting_entry.pack()
        print(self.fasting_entry.get())

        # self.submit_button = tk.Button(self.main_frame, text="Submit", command=self.submit_clicked)
        # self.submit_button.pack(pady=10)

def application():
    root = tk.Tk()
    view = MainView(root)
    root.mainloop()

if __name__ == "__main__":
    application()
