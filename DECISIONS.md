# Design Decisions

## Day 1: PDF extraction

### 1. Why store the page number at extraction time?
Chunking merges and splits text, and after that the page boundaries are gone. The only reliable moment to record which page text came from is while reading page by page. Citations ("answer found on page 4") depend on it. Adding it later would mean re-extracting and re-ingesting every document.

### 2. What does get_text() return for a scanned PDF?
An empty string. A scanned PDF stores each page as an image, with no text layer for PyMuPDF to read. Extracting that text needs OCR (a separate step), which is out of scope for version 1.

### 3. Why raise ValueError instead of returning an empty list?
An empty list looks like success. The pipeline would go on to store zero chunks, and later every question would get "not found in the document", with no hint that the PDF was unreadable. A clear error lets the API return a useful message to the user ("this looks like a scanned PDF") and fails at the real source of the problem.
