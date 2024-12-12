from PyPDF2 import PdfReader, PdfWriter

# Load the PDF file
input_pdf = "test12.pdf"  # Replace with the path to your PDF file
output_pdf = "test12_with_keywords.pdf"

# Create a reader to read the original PDF
reader = PdfReader(input_pdf)

# Create a writer to create the new PDF
writer = PdfWriter()

# Copy all pages from the original PDF to the new PDF
for page in reader.pages:
    writer.add_page(page)

# Add metadata
metadata = {
    "/Title": "Sample PDF Title",
    "/Author": "Author Name",
    "/Subject": "Adding Metadata Example",
    "/Keywords": "example, metadata, PyPDF2, keywords",
}
writer.add_metadata(metadata)

# Save the new PDF
with open(output_pdf, "wb") as output_file:
    writer.write(output_file)

print(f"Metadata successfully added to {output_pdf}")
