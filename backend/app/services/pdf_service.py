import pymupdf

def extract_pages(pdf_path):
    # 1. Try to open the file; if it fails, raise a clear error
    try:
        doc = pymupdf.open(pdf_path)
    except Exception as e:
        raise ValueError("Could not open file as a PDF") from e

    # 2. Encrypted check
    if doc.needs_pass:
        doc.close()
        raise ValueError("PDF is password-protected")

    pages = []
    for i, page in enumerate(doc):
        text = page.get_text().strip()
        if not text:                      # skip pages with no text
            continue
        pages.append({"page": i + 1, "text": text})

    doc.close()

    # 3. Nothing found at all
    if not pages:                          # the list is empty
        raise ValueError("No extractable text (possibly a scanned PDF)")

    return pages