import tkinter as tk
from tkinter import filedialog

def select_file():
    root = tk.Tk()
    root.withdraw()  # A gyökér ablakot elrejtjük
    
    file_path = filedialog.askopenfilename(title="Válaszd ki az inputfájlt! (.xlsx, .xls)")  # Fájl kiválasztása ablak megjelenítése
    
    if file_path:
        print("Selected file:", file_path)
        return file_path
    else:
        print("No file selected.")

if __name__ == "__main__":
    select_file()
