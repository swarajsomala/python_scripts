import PyPDF2
pdfFileObj = open('AUTOSAR_SWS_RTE.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages
pageObj = pdfReader.getPage(0)
pageObj.extractText()