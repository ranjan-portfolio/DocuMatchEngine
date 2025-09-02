# DocuMatchEngine

DocuMatchEngine is an AI-driven test suite designed to validate the structure and content of document templates. It matches data from XML files to placeholders in DOCX templates and ensures the generated PDF output aligns with expectations.

## Inputs

1. **Excel File:** Contains data items and their statuses (mandatory/optional).
2. **XML Data:** Provides placeholder data for document generation.
3. **DOCX Template:** The document template containing placeholders, conditions, and static text.
4. **Generated PDF:** The final output document to be validated.

---

## Processing Stages

1. **Read Excel File:** Extract test cases and identify items marked as mandatory or optional.
2. **Validate XML Data:** 
    - Check if all mandatory items are present in the XML.
    - **Pass:** Proceed to Stage 3.
    - **Fail:** Mark the test case as failed, listing missing mandatory items.
3. **Process DOCX Template:**
    - Extract content (placeholders, conditions, loops, static text) from the DOCX.
    - Apply XML data to generate the expected content text.
4. **Content Validation:**
    - Check if the generated content matches expectations.
    - **Pass:** Proceed to Stage 5.
    - **Fail:** Obtain LLM (Large Language Model) feedback, update input, and retry Stage 3.
5. **PDF Validation:**
    - Extract and compare the text content of the supplied PDF with the output from Stage 4.
    - **Pass:** Test passes if everything matches.
    - **Fail:** Test fails with detailed reasoning.

---

## Outputs

- **Pass:** Test cases are successfully validated with a confidence factor.
- **Fail:** Test cases fail with a detailed list of textual discrepancies.

---

## Overview

DocuMatchEngine streamlines the verification of document templates, leveraging AI to automate content checks and ensure high-quality, consistent outputs across document types.
