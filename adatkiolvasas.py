import pandas as pd

# Excel fájl elérési útja
excel_file = 'hirlevel_input.xlsx'

# Excel fájl beolvasása DataFrame-be
df = pd.read_excel(excel_file)

# DataFrame megjelenítése
print(df)

# Az első oszlop a címeket tárolja
cimek = df['CIM']

# A második oszlop a bevezetőket tárolja
bevezetok = df['BEVEZETO']

# A harmadik oszlop a hivatkozásokat tárolja
hivatkozasok = df['HIVATKOZAS']

# A negyedik oszlop a nyitókép hivatkozásokat tárolja
nyitokep_hivatkozasok = df['NYITOKEP_HIVATKOZAS']

print(cimek)


def generate_output(input_html, data, output_file):
    # Változók definiálása
    VALTOZO_NYITOKEP_HIVATKOZAS = 'VALTOZO_NYITOKEP_HIVATKOZAS'
    VALTOZO_HIVATKOZAS = 'VALTOZO_HIVATKOZAS'
    VALTOZO_CIM = 'VALTOZO_CIM'
    VALTOZO_BEVEZETO = 'VALTOZO_BEVEZETO'

    # Adatok beillesztése a HTML fájlba
    output_html = input_html.replace(VALTOZO_NYITOKEP_HIVATKOZAS, data['NYITOKEP_HIVATKOZAS'])
    output_html = output_html.replace(VALTOZO_HIVATKOZAS, data['HIVATKOZAS'])
    output_html = output_html.replace(VALTOZO_CIM, data['CIM'])
    output_html = output_html.replace(VALTOZO_BEVEZETO, data['BEVEZETO'])

    # Az eredmény kiírása az output fájlba
    with open(output_file, 'a', encoding='utf-8') as f:
        f.write(output_html)



# Excel fájl beolvasása DataFrame-be
df = pd.read_excel(excel_file)

# Az input HTML fájl beolvasása
with open('part.html', 'r', encoding='utf-8') as f:
    input_html = f.read()

# Az Excelből beolvasott adatok beillesztése
for index, data in df.iterrows():
    generate_output(input_html, data, 'output_part.html')









def insert_part(input_file, part_file, output_file):
    # Input HTML fájl beolvasása
    with open(input_file, 'r', encoding='utf-8') as f:
        input_html = f.read()

    # part.html fájl beolvasása
    with open(part_file, 'r', encoding='utf-8') as f:
        part_html = f.read()

    # Beszúrás az input HTML fájlba
    index_to_insert = input_html.find('<!-- Insert part.html here -->')
    if index_to_insert != -1:
        output_html = input_html[:index_to_insert] + part_html + input_html[index_to_insert:]
    else:
        # Ha nem találjuk meg a beszúrás helyét, akkor csak az eredeti HTML-t használjuk
        output_html = input_html

    # Írjuk ki az eredményt az output fájlba
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output_html)

# Fájlok elérési útjainak beállítása
input_file_path = 'hirlevel.html'
part_file_path = 'output_part.html'
output_file_path = 'output.html'

# Beszúrás végrehajtása
insert_part(input_file_path, part_file_path, output_file_path)


