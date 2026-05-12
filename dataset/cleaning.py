import pandas as pd

df = pd.read_csv("dataset_with_text.csv")

# Remove empty OCR rows
df = df[df["ocr_text"].notna()]

# Remove very short text
df = df[df["ocr_text"].str.len() > 3]

# Save cleaned dataset
df.to_csv("cleaned_dataset.csv", index=False)

print("Cleaned dataset saved")
print("Remaining memes:", len(df))
