import PyPDF2

# create a pdf file object
pdfFileObj = open("hs.pdf",'rb')

# create pdf file reader
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# display total pages
print(pdfReader.numPages)

# create a text file object
textObj = pdfReader.getPage(0)

#extract text from the page
print(textObj.extractText())

# close
pdfFileObj.close()