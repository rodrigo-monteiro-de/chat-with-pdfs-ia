from pypdf import PdfReader

#============================
#Ingestion Pipeline
#============================

pdfPath = "data/Softwares_modelagem.pdf"
reader = PdfReader(pdfPath)

print(f"Pages found: {len(reader.pages)}")

all_text =""

for page in reader.pages:
    
    text = page.extract_text()
    
    if text:
        all_text += text
 
#count = len(all_text[:1000])
#print(count)

#print(all_text[:1000])

chunk_size = 150

chunks = []

for i in range (0, len(all_text),chunk_size):
    chunks.append(all_text[i:i+ chunk_size])

print(f"Chunks created: {len(chunks)}")

print(chunks[0])
print("-------------")
print(chunks[1])
print("-------------")
print(chunks[2])
