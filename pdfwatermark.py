import PyPDF2
import sys

pdf_file = sys.argv[1]
pdf_watermark = sys.argv[2]

template = PyPDF2.PdfFileReader(open(f'{pdf_file}.pdf','rb'))
watermark = PyPDF2.PdfFileReader(open(f'{pdf_watermark}.pdf','rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
	page = template.getPage(i)
	page.mergePage(watermark.getPage(0))
	output.addPage(page)

	with open('output_pdf.pdf','wb') as file:
		output.write(file)