from PyPDF2 import PdfWriter

merger = PdfWriter()

pdfs=[]
n=int(input("Enter the number of PDFs to merge: \n"))

for i in range(0,n):
    name=input(f"Enter the name of PDF {i+1} (with .pdf extension): ")
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()