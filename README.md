# pdf-extractor

This repo consists of two python scripts: pdf_reader_general, which extracts all text from a pdf without formatting, and pdf_reader_table, which extracts tables from a PDF and exports them into an Excel file.

## pdf_reader_general
The library required is PyPDF2, used for working with PDFs in Python.

The code iterates over each page or a specified number of pages (using page_num), extracting text from said pages, and appending the text to an empty string. Trailing and leading whitespaces are removed before displaying the text. However the text and tables are unformatted. 


## pdf_reader_table
The libraries required are "pandas" for working with structured data and "read_pdf" from "tabula.io", used to read tables from PDF files.

Use the read_pdf function to read tables from a specified pdf ("sample.pdf" in this case), specify which pages to read from (e.g. pages = "1"), and if multiple tables exist on each page, which tables should be extracted (multiple_tables=True extracts all tables, while multiple_tables=False only extracts the first table on a page).

Given the name of the Excel file where the extracted tables will be saved (tables_extracted.xlsx), each extracted table/dataframe will be written into the Excel file as a different sheet, with names generated as "Table_1", "Table_2", etc. A confirmation message is printed at the end, indicating where the extracted tables are saved.

To view the tables instead of or in addition to exporting the tables to an Excel file, import the tabulate library, used to display tables in a readable manner (commented out in the given script). 

Use the tabulate function, to specify the dataframe (df in this case, the code iterates over each of the dataframes extracted from the PDF) and what format the tables are to be displayed as (tablefmt = 'psql' means PostgreSQL style, but can also be displayed in other styles including grid and html).
