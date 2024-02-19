from adatkiolvasas import generatePartOutPut, insert_part
from selectInputFile import select_file





# Fájlok elérési útjainak beállítása
input_file_path = '/Users/bognarlehel/Lehel/Github/hirlevelGeneralas/template/template.html'
input_part_file_path='/Users/bognarlehel/Lehel/Github/hirlevelGeneralas/template/part.html'

output_part_file_path =  'output_part.html'
output_file_name = 'output.html'
# Excel fájl elérési útja
excel_file = select_file()

#OutputPart generál
# ás
generatePartOutPut(input_part_file_path, excel_file)

# Beszúrás végrehajtása
insert_part(input_file_path, output_part_file_path, output_file_name)

