# Code

## quader.py

A python script to double up each page of a PDF for printing two page blocks at once.

> python quader.pdf source_pdf result_pdf



### Requirements

* PyPDF2
* pathlib

### Needed Improvements

* Add an optional parameter for setting the resulting number of pages to scale each page by. (default value: 4)

## deimposer.py

A python script that takes a PDF resulting from an imposed A4 PDF being sliced, and sorts the resulting pages into the correct oder

> python deimposer.py source_pdf result_pdf

### Requirements

* PyPDF2
* pathlib

### Needed Improvements

* Refactor to share code with quader.py

# Other
## regex.md
Holds regex patterns I've found useful while preparing texts for printing (tested with Sublime Text 3).
