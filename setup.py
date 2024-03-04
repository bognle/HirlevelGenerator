#FOR MAC

#from setuptools import setup
#
#setup(
#    app=["main.py"],
#    setup_requires=["py2app"],
#    data_files=[('template', ['template/part.html', 'template/template.html'])]  # Itt add meg a template mappád tartalmát
#)
#



#FOR WINDOWS

from setuptools import setup
import py2exe

setup(
    console=["main.py"],  # Módosítsuk console-ra, ha parancssori alkalmazást készítünk
    options={
        "py2exe": {
            "packages": ["tkinter"],  # Ha a program használja a tkinter modult
            "includes": ["tkinter", "tkinter.filedialog", "tkinter.messagebox"]  # Szükséges modulok listája
        }
    },
    data_files=[
        ('template', ['template/part.html', 'template/template.html'])
    ]
)