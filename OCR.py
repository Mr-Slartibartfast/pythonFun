from PIL import Image
import pytesseract
import pandas as pd
import shutil
import os

# load the image - set this to the path of the image
image = Image.open("image-file-path.png")

# use tesseract OCR to extract text from the image
text = pytesseract.image_to_string(image)

# split the extracted text into words
words = text.split()

# create a pandas data frame to display the words in a table
data = pd.DataFrame({"Words": words})

csv_filename = "ocr_words.csv"

data.to_csv(csv_filename, index=False)


# display the table
#print(data)
desktop_path = os.path.expanduser("~/Desktop")

shutil.move(csv_filename, os.path.join(desktop_path, csv_filename))



