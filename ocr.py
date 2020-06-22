import sys
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
#pass in path to photo as command line arg
image = cv2.imread(str(sys.argv[1]))
text = pytesseract.image_to_string(image)

print(text)


#python ocr.py photos\\IMG-20200622-WA0000.jpg