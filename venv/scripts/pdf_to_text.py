import fitz
def pdf_to_text(file_path:str)->str:
    doc = fitz.open(file_path)
    text = []
    for page_num in range(len(doc)):
        page = doc[page_num]
        text.append(page.get_text())  # Extract text from page
    doc.close()
    return "\n".join(text)