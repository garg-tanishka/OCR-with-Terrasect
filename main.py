import pytesseract
from PIL import Image
import pandas as pd
import re

def parse_image(img_path):
    corpus = []
    result = pytesseract.image_to_string(Image.open(img_path))  # Recognize text with tesseract for python
    corpus.append(result)
    return corpus

def clean(text):
    return re.sub('[^A-Za-z0-9" "]+', ',', text)

def create_df():
    corpus = parse_image(filename)
    data = pd.DataFrame(list(corpus), columns=['sample'])
    data['Cleaned_sample'] = data['sample'].apply(clean)
    data.to_csv("output.csv", index=False)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Path of image
    filename = 'xxxx' #Enter the image path here
    create_df()
