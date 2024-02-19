from adatkiolvasas import generatePartOutPut, insert_part

# Fájlok elérési útjainak beállítása
input_file_path = 'template/template.html'
part_file_path = 'output_part.html'
output_file_name = 'output.html'

#OutputPart generálás
generatePartOutPut()

# Beszúrás végrehajtása
insert_part(input_file_path, part_file_path, output_file_name)

