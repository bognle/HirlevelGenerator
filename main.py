from adatkiolvasas import generatePartOutPut, insert_part
from selectInputFile import select_file
import tkinter as tk
from tkinter import filedialog



# Fájlok elérési útjainak beállítása
input_file_path = 'template/template.html'
input_part_file_path='template/part.html'

output_part_file_path =  'output_part.html'
output_file_name = 'output.html'
# Excel fájl elérési útja
excel_file = select_file()
#OutputPart generál
# ás
generatePartOutPut(input_part_file_path, excel_file)

try:
    # Beszúrás végrehajtása
    insert_part(input_file_path, output_part_file_path, output_file_name)


except Exception as e:
    # Ha valamilyen hiba történik, az kivételt dob, és ide kerülünk
    print("Hiba történt:", e)  # Kiírjuk a hibaüzenetet a konzolra
    root = tk.Tk()
    root.withdraw()  # A gyökér ablakot elrejtjük
    
    folder_path = filedialog.askdirectory(title="Kérlek válaszd ki hogy hova szeretnéd menteni a fájlt!")

