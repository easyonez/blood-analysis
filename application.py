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
        self.title = tk.Label(self.main_frame, text="Blood Analysis 1.0.2")
        self.title.pack()
        self.label = tk.Label(self.main_frame, text="Welcome to Blood Analysis!")
        self.label.pack(pady=10)        
        self.button = tk.Button(self.main_frame, text="Click Me", command=self.button_clicked)
        self.button.pack(pady=10)
        
    def button_clicked(self):
        self.button.destroy()
        self.root.geometry("500x400")
        self.label.config(text="Please enter your information")

        self.name_label = tk.Label(self.main_frame, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.main_frame)
        self.name_entry.pack()


        self.age_label = tk.Label(self.main_frame, text="Age:")
        self.age_label.pack()
        self.age_entry = tk.Entry(self.main_frame)
        self.age_entry.pack()

        self.fasting_label = tk.Label(self.main_frame, text="Fasting? (y/n):")
        self.fasting_label.pack()
        self.fasting_entry = tk.Entry(self.main_frame)
        self.fasting_entry.pack()
        self.submit_button = tk.Button(self.main_frame, text="Submit", command=self.submit_clicked)
        self.submit_button.pack(pady=10)


    def submit_clicked(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        fasting = self.fasting_entry.get()
        self.information_label = None
        if fasting == "y":
            fasting = True
        elif fasting == "n":
            fasting = False
        else:
            self.information_label = tk.Label(self.main_frame, text="Invalid input")
            self.information_label.pack()
            return
        entry_list = [name, age, fasting]
        print(entry_list)
        self.fasting_label.destroy()
        self.fasting_entry.destroy()
        self.age_label.destroy()
        self.age_entry.destroy()
        self.name_label.destroy()
        self.name_entry.destroy()
        self.submit_button.destroy()
        if self.information_label != None:
            self.information_label.destroy()
        self.tests()

    def tests(self):
        self.label.config(text="Please select the tests you would like to take")
        self.test_list = tk.Listbox(self.main_frame, selectmode=tk.MULTIPLE)
        for item in blood_test_items:
            self.test_list.insert(tk.END, item)
        self.test_list.pack()
        self.submit_tests_button = tk.Button(self.main_frame, text="Submit Tests", command=self.submit_tests)
        self.submit_tests_button.pack(pady=10)

    def submit_tests(self):
        selected_tests = self.test_list.curselection()
        print(selected_tests)
        self.label.config(text="Thank you for submitting your tests")
        self.test_list.destroy()
        self.submit_tests_button.destroy()  


def application():
    root = tk.Tk()
    view = MainView(root)
    root.mainloop()

if __name__ == "__main__":
    application()
