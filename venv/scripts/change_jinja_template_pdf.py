import fitz

def change_jinja_to_pdf(template :str):
  pdf = fitz.open()  # empty PDF
  page = pdf.new_page()  # add a page
  # Define a rectangle for the page margins
  rect = fitz.Rect(50, 50, 550, 800)  # left, top, right, bottom in points

# Insert text with wrapping
  page.insert_textbox(
    rect,
    template,
    fontsize=12,
    fontname="helv",
    align=0  # 0=left, 1=center, 2=right, 3=justify
)

  pdf.save("output_letter.pdf")
  pdf.close()
