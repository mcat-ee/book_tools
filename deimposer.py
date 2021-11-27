
from PyPDF2 import PdfFileWriter,PdfFileReader
from pathlib import Path
import sys


def grouper(reader, group_size):
    number_of_pages = reader.getNumPages()
    number_of_batches = int(number_of_pages/group_size)
    print(f"Number of groups to generate: {number_of_batches}")
    batches = []

    for batch_number in range(number_of_batches):
        batch_start = batch_number * group_size
        current_batch = [reader.getPage(batch_start), reader.getPage(batch_start+1),reader.getPage(batch_start+2), reader.getPage(batch_start+3)]
        batches.append(current_batch)
    return batches


def get_file(filename):
    input_pdf = PdfFileReader(str(filename))
    return input_pdf


def arrange_pages(file_contents):
    number_of_pages = file_contents.getNumPages()
    book_arrangement = PdfFileWriter()
    print("Page count:", number_of_pages)
    batches = grouper(file_contents, 4)
    for batch in batches:
        book_arrangement.addPage(batch[1])
        book_arrangement.addPage(batch[2])

    for batch in reversed(batches):
        book_arrangement.addPage(batch[3])
        book_arrangement.addPage(batch[0])

    return book_arrangement

def save_to_file(arrangement, output_filename):
    with Path(output_filename).open(mode="wb") as output_file:
        try:
            arrangement.write(output_file)
        except: 
            print("ERROR!")

INPUT_FILENAME = sys.argv[1]
OUTPUT_NAME = sys.argv[2]
file_contents = get_file(INPUT_FILENAME)
result_object = arrange_pages(file_contents)
save_to_file(result_object, OUTPUT_NAME)
