from PyPDF2 import PdfReader

file = open('schaffer.pdf', 'rb')
pdf = PdfReader(file)

# Create an output text file
with open('output.txt', 'w') as output:
    # Iterate through the pages of the PDF
    for i in range(len(pdf.pages)):
        # Exclude certain pages
        if i+1 not in [0,1,2]:
            # Extract the text from the current page
            text = pdf.pages[i].extract_text()
            # Write the text to the output file
            output.write(text)
file.close()

