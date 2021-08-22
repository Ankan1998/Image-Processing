from PyPDF2 import PdfFileWriter, PdfFileReader
import os

def pdf_splitter(file,page_per_pdf):
    inputpdf = PdfFileReader(open(file, "rb"))
    len_pdf = inputpdf.numPages
    list_ = list(range(0,len_pdf,page_per_pdf))
    for idx,_ in enumerate(list_):
        if idx+1 != len(list_):
            output = PdfFileWriter()
            for page in range(list_[idx],list_[idx+1]):
                data = inputpdf.getPage(page)
                output.addPage(data)
            with open(os.path.splitext(os.path.basename(file))[0] + "_page%s.pdf" % idx, "wb") as outputStream:
                output.write(outputStream)
        else:
            output_f = PdfFileWriter()
            for page in range(list_[idx], len_pdf):
                data_f = inputpdf.getPage(page)
                output_f.addPage(data_f)
            with open(os.path.splitext(os.path.basename(file))[0] + "_page%s.pdf" % idx, "wb") as outputStream:
                output_f.write(outputStream)