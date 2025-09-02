from langchain_core.prompts import ChatPromptTemplate
from scripts.llm import invoke_llm

def match_pdf_with_template_text_prompt(template_text,pdf_text):
    template="""You are a document tester.
    Given an template_text and pdf_text. Compare template_text with pdf_text and output if template_text and pdf_text
    are exact match. If they are not exact match output the difference between template_text and pdf_text.
    this is template_text: {template_text}
    this is pdf_text: {pdf_text}
    """
    prompt=ChatPromptTemplate.from_template(template=template)
    final_prompt=prompt.format_messages(template_text=template_text,pdf_text=pdf_text)
    return final_prompt

 

def mark_test_case(llmresponse: str)->str:
    template="""
        You are a tester. 
        Given a llm response which compares a jinja template output and a pdf output and provides is response
        Determine if the test case has passed or failed
        Provide output in following format
        ✅ Test case passed with reason and a confidence factor
        or
        ❌ Test case failed with reason and a confidence factor
        Here is the llm response
        {response}
    """
    prompt=ChatPromptTemplate.from_template(template=template)
    final_prompt=prompt.format_messages(response=llmresponse)
    response=invoke_llm(final_prompt)
    return response