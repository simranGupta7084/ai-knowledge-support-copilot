from app.services.pdf_service import extract_pages

for p in extract_pages("../data/sample.pdf"):
    print(p["page"], len(p["text"]), p["text"][:80].replace("\n", " "))
