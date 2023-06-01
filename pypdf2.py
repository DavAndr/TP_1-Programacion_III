import PyPDF2

pdf = open("Velas.pdf", "rb")
output_file = open("texto_extraido.txt", "w", encoding="utf-8")

reader = PyPDF2.PdfReader(pdf)

for no_page in range(len(reader.pages)):
    output_file.write("Pagina " + str(no_page+1) + "\n")
    info_page = reader.pages[no_page]
    extract_info = info_page.extract_text()
    output_file.write("******************\n")
    output_file.write(extract_info + "\n")
    output_file.write("******************\n")

output_file.close()
pdf.close()