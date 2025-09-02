
import os
from jinja2 import Template
from scripts.xml_to_dict import xml_to_dict
from scripts.read_docx import readddocxfile
from scripts.changedocx_to_jinja import changedocx_to_jinja
from scripts.change_jinja_template_pdf import change_jinja_to_pdf
from scripts.pdf_to_text import pdf_to_text
from scripts.llm import get_llm_model,invoke_llm
from scripts.prompts import match_pdf_with_template_text_prompt,mark_test_case




if __name__== "__main__":
    current_dir=os.path.dirname(__file__)
    xml_path=os.path.join(current_dir,"xml","organization-data.xml")
    dict=xml_to_dict(xml_path)
    docx_path=os.path.join(current_dir,"template","Change_of_address.docx") 
    template_text=readddocxfile(docx_path)
    #print(f"Template text::::: {template_text}")
    jinja_output_text=changedocx_to_jinja(template_text,dict)
    print(f"Jina output text::: {jinja_output_text}")
    #change_jinja_to_pdf(jinja_output_text)
    pdf_path=os.path.join(current_dir,"pdf","organization_letter.pdf")
    pdf_text=pdf_to_text(pdf_path)
    print(f"PDF output text::: {pdf_text}")
    prompt=match_pdf_with_template_text_prompt(jinja_output_text,pdf_text)
    llmresponse=invoke_llm(prompt)
    print(llmresponse)
    test_verdict=mark_test_case(llmresponse)
    print(test_verdict)




 
    