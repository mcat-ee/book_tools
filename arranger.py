
from PyPDF2 import PdfFileWriter,PdfFileReader
from pathlib import Path
import sys
#page = pdf_writer.addBlankPage(width=72, height=72)

OUTPUT_NAME = sys.argv[2]
INPUT_FILENAME = sys.argv[1]



def get_file(filename):
	input_pdf = PdfFileReader(str(filename))
	return input_pdf


def arrange_pages(file_contents):
	number_of_pages = file_contents.getNumPages()
	book_arrangement = PdfFileWriter()
	for page_number in range(number_of_pages):
		page = file_contents.getPage(page_number)
		book_arrangement.addPage(page)
		book_arrangement.addPage(page)
	return book_arrangement

def save_to_file(arrangement, output_filename):
	with Path(output_filename).open(mode="wb") as output_file:
		arrangement.write(output_file)

file_contents = get_file(INPUT_FILENAME)
result_object = arrange_pages(file_contents)
save_to_file(result_object, OUTPUT_NAME)