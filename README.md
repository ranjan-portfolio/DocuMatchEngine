# DocuMatchEngine
The project takes an attempt to create a test suite leveraging AI to match document template structure and content with xml data and a generated pdf

## Input

1. Excel file containing dataitems and status (mandatory/optional)
2. xml data containing document placeholder data
3. docx file contianing document template (Template contains [placeholder] ,[conditions] and static word)
4. generated pdf
##

## Processing stages:

1 Read excel file for the test case containing data item marked marked optional or mandatory
2.Check if xml has all the mandatory items
	2.1 Pass --> Move to stage 3
	2.2 Fail --> Mark case as failed (Mandatory items not present in xml, mention the data item)
3.Scrap document content from docx (docx contains placeholder,conditions,loops and wordings) and apply xml data
  and generate the content text
4.Check if generated content is correct
	4.1 Pass --> Move to stage 5
	4.2 Fail --> Get the llm response and feed it to stage 3 to regenerate
5.Scrap supplied pdf document content and check if pdf text content matches with Stage 4 output
	5.1 Everything matches pass the test
	5.2 Fail the test with reasoning

## Output:

Pass the test cases with confidence factor
Fail the test cases and provide the list of textual discrepancy
