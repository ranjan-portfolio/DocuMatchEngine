# DocuMatchEngine

DocuMatchEngine is an AI-driven test suite designed to validate the structure and content of document templates. It matches data from XML files to placeholders in DOCX templates and ensures the generated PDF output aligns with expectations.

## Inputs

1. **XSD or DTD file:** For validating xml structure.
2. **XML Data:** Provides placeholder data for document generation.
3. **DOCX Template:** The document template containing placeholders, conditions, and static text.
4. **PDF:** The pdf document to be validated.

---

## Processing Stages

1. **Loads XML file and DTD/XSD and validates structure:**
2. **Process DOCX Template:**
    - Extract content (placeholders, conditions, loops, static text) from the DOCX.
3. ** Attempts to convert DOCX Template into Jinja Template **
4. ** Jinja template is used to render pdf with all data placeholders replaced with xml data and logical conditions evaluated **
5. ** Extracts pdf output generated in point 4 **
6. ** Extracts pdf output from the pdf document to be tested **
7. **Content Validation:**
    - Passes Jinja template pdf and test pdf for content matching 
8. **Marks the testcase pass or fail based on llm output from point 7:**
    - **Pass:** Test passes if everything matches with reasoning and confidence score.
    - **Fail:** Test fails with detailed reasoning and confidence score.

---

## Outputs

- **Pass:** Test cases are successfully validated with a confidence factor.
- **Fail:** Test cases fail with a detailed list of textual discrepancies.

---

## Overview

DocuMatchEngine streamlines the verification of document templates, leveraging AI to automate content checks and ensure high-quality, consistent outputs across document types.
