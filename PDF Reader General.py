import PyPDF2

# Open the PDF file
PDFfile = open('sample.pdf', 'rb')

# Create a PdfReader object
PDFfilereader = PyPDF2.PdfReader(PDFfile)

# Initialize an empty string to store all text
all_text = ""

# Iterate over all pages
for page_num in range(len(PDFfilereader.pages)):
    # Get a specific page
    page = PDFfilereader.pages[page_num]

    # Extract text from the page
    page_text = page.extract_text()

    # Append the extracted text to the string
    all_text += page_text

    # Optionally, print the text of each page
    print(f"Text from page {page_num + 1}:")
    print(page_text.strip())  # strip() removes leading and trailing whitespace
    print("-----------------------------")

# Print all extracted text
print("\n\nAll extracted text from the PDF:")
print(all_text.strip())  # Strip() to remove leading and trailing whitespace

# Close the PDF file
PDFfile.close()

