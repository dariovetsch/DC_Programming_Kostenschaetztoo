import tkinter as tk
from Interface import GUI
from Cost_Calculation import calculate_costs
from Presentation import presentation
from Extra import extra_cost

def main():
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
    # You can call calculate_costs and presentation functions within the GUI after user interaction
    calculate_costs()  # Call this function when appropriate within the GUI
    extra_cost ()
    presentation()     # Call this function when appropriate within the GUI
    

