import pdfplumber
import pandas as pd

with pdfplumber.open("data.pdf") as pdf:
    # Extract all text from the first page
    text = pdf.pages[0].extract_text()

if text:
    # Split text into lines and then into columns based on spaces
    lines = [line.split() for line in text.split('\n')]
    
    # Save to Excel
    df = pd.DataFrame(lines)
    df.to_excel("output.xlsx", index=False, header=False)
    print("Success! Created output.xlsx using text extraction.")
else:
    print("Error: The PDF is empty or is an image/scan.")