# PDF Merger

A simple Python script to merge multiple PDF files into a single PDF using `PyPDF2`'s `PdfWriter`.

---

## Features

- Merge any number of PDF files
- Easy command-line input for PDF filenames
- Saves the merged PDF as `merged-pdf.pdf`

---

## Requirements

- Python 3.x
- PyPDF2 library

Install PyPDF2 if you don’t have it yet:

```bash
pip install PyPDF2
```

# Usage
1. Place all the PDF files you want to merge in the same folder as the script.
2. Run the script:
   ```bash
   python merge_pdfs.py
   ```
3. Enter the number of PDFs to merge.
4. Enter the filenames of each PDF (including the .pdf extension).
5. The merged PDF will be saved as merged-pdf.pdf in the same folder.

# Example
```bash
Enter the number of PDFs to merge:
3
Enter the name of PDF 1 (with .pdf extension): file1.pdf
Enter the name of PDF 2 (with .pdf extension): file2.pdf
Enter the name of PDF 3 (with .pdf extension): file3.pdf

Successfully merged PDFs into 'merged-pdf.pdf'
```

# Notes
- Make sure the PDF files exist in the folder before running the script.

- The output file merged-pdf.pdf will be overwritten if it already exists.

- This script uses PdfWriter from PyPDF2 (version 3.0.0 or later) which supports the append() method to merge PDFs.
