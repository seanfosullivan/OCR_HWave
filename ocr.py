import sys
import pytesseract
import pandas as pd
import difflib
from PIL import Image
import PIL.ImageOps   

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


#pass in path to photo as command line arg
image = Image.open(str(sys.argv[1]))
inv_image = PIL.ImageOps.grayscale(image) 
inverted_image = PIL.ImageOps.solarize(inv_image, threshold=128)
test=PIL.ImageOps.autocontrast(inverted_image, cutoff=0)
text = pytesseract.image_to_string(test)
'''
inv_image = PIL.ImageOps.invert(image)
inv_text = pytesseract.image_to_string(inv_image)
print(inv_text)
'''
df = pd.read_csv("test.csv")
products=df['product'].to_list()
prices=df['price'].to_list()
print(text)
print(difflib.get_close_matches(text,products))


#python ocr.py photos\\IMG-20200622-WA0000.jpg

'''
const spawn = require("child_process").spawn;
const pythonProcess = spawn('python',["path/to/script.py", arg_photo]);
'''