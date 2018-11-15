## testing PILlow library
import PIL
from PIL import Image


import tkinter as tk
import tkinter.ttk as ttk
from tkcolorpicker import askcolor

#root = tk.Tk()
#style = ttk.Style(root)
#style.theme_use('clam')

testRGB = askcolor()
print(testRGB)
#print(askcolor((255, 255, 0), root))

#img = Image.open('/Users/adamb/Downloads/classic-DD-party.png')
#img.show()
