#https://pypi.org/project/pytesseract/
#Extracting content of a image using tesseract-OCR application
"""
Step 1:Install tesseract-OCR application

Syep 2:Download required libraries which is :
        1)pip install Pillow for image
        2)pip install pytesseract

Step 3:
Import the pytesseract for extraction of the content and PIL for image
Copy the path where tesseract-OCR application is intalled.
"""
import pytesseract as tess
tess.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
from PIL import Image

img=Image.open('c3.png')
text=tess.image_to_string(img)
print(text)
