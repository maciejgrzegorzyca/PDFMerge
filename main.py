import PyPDF2
import os
import re

#funkcja zcalajaca
def PDFmerge(pdfs, output):
    pdfmerge = PyPDF2.PdfFileMerger()

    for pdf in pdfs:
        pdfmerge.append(pdf)

    with open(output, "wb") as f:
        pdfmerge.write(f)

def main():
    only_pdfs = []                                 #lista tylko plikow pdf
    with_dir = []                                #lista plikow z dodana sciezka
    arr = os.listdir("D:/PDF/")                  #sciezka z korej pobiera sie pliki


    w1 = r"(\w*\.pdf)"                       #warunek wyszukania .pdf
    for i in arr:
        m1 = re.findall(w1, i)                  #sprawdzneie ****.pdf
        only_pdfs += m1                         #dodanie do listy z pdfamie



    for files in only_pdfs:                         #dodanie do plikow nazwy sciezki
        with_dir.append(f"D:/PDF/{files}")

    output = "D:/PDF/com.pdf"                   #gdzie ma byc zcalony plik
    PDFmerge(pdfs=with_dir, output=output)      #wywolanie funkci scalenia z dwoma argumentami

if __name__ == '__main__':                      #wywolanie
    main()