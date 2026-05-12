import os
import pandas as pd

folder = "9gag_memes"

data = []

for img in os.listdir(folder):
    data.append({
        "image": img,
        "ocr_text": "",
        "label": ""
    })

df = pd.DataFrame(data)

df.to_csv("dataset.csv", index=False)

print("CSV created")
