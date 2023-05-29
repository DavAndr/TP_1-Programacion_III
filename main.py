import PyPDF2

pdf = open("velas.pdf", "rb")

reader = PyPDF2.PdfReader(pdf)

for no_page in range(len(reader.pages)):
    print("Pagina ",no_page+1)
    info_page =reader._get_page(no_page)
    extract_info = info_page.extract_text()
    print(extract_info)
    print("******************")