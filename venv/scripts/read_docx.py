from docx import Document

def readddocxfile(path:str)->str:
    doc=Document(path)
    text=[]
    for para in doc.paragraphs:
        text.append(para.text)
    return "\n".join(text)