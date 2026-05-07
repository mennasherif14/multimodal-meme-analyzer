import pandas as pd
import pytesseract
from PIL import Image
import os

# Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Read CSV
df = pd.read_csv("dataset.csv")

# Empty list for OCR text
ocr_texts = []

# Loop through images
for img in df["image"]:

    path = os.path.join("9gag_memes", img)

    try:
        # Open image
        image = Image.open(path)

        # Resize image (improves OCR accuracy)
        image = image.resize((image.width * 2, image.height * 2))

        # Convert to grayscale
        image = image.convert("L")

        # Apply thresholding
        image = image.point(lambda x: 0 if x < 140 else 255)

        # OCR extraction
        text = pytesseract.image_to_string(
            image,
            config="--psm 6"
        )

        # Clean text
        text = text.strip()

        print(f"OCR done for: {img}")
        print(text)
        print("-" * 50)

    except Exception as e:
        print(f"Error with {img}: {e}")
        text = ""

    ocr_texts.append(text)

# Add OCR column
df["ocr_text"] = ocr_texts

# Save new CSV
df.to_csv("dataset_with_text.csv", index=False)

print("DONE")