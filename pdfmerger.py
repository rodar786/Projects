from PyPDF2 import PdfMerger

pdfs = ["first.pdf", "second.pdf"]

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)


merger.write("merged.pdf")
merger.close()