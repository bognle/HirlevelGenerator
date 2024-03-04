import tkinter as tk
from tkinter import filedialog

def select_folder():
    try:
    
        root = tk.Tk()
        root.withdraw()  # A gyökér ablakot elrejtjük
        
        folder_path = filedialog.askdirectory(title="Kérlek válaszd ki hogy hova szeretnéd menteni a fájlt!")  # Mappa kiválasztása ablak megjelenítése
        
        if folder_path:
            print("Selected folder:", folder_path)
            return folder_path
        else:
            print("No folder selected.")
    except Exception as e:
        print("itt mi a hiba",e )

if __name__ == "__main__":
    select_folder()