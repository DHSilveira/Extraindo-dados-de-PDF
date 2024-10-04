import PyPDF2

pdf_file_path = r'C:\Users\Usuario\Favorites\Área de Trabalho\python\code.py\Extraindo dados de PDF\livros-pdf\qualquer.pdf'

def extrair_texto_paginas(pdf, paginas):
    total_paginas = len(pdf.pages)
    
    for pagina in paginas:
        if 0 <= pagina < total_paginas:
            pg = pdf.pages[pagina]
            texto_formatado = ''.join(pg.extract_text())
            print(f"\nTexto da página {pagina}:\n")
            print(texto_formatado)
        else:
            print(f"Página {pagina} está fora do limite (0 a {total_paginas}).")

def selecionar_paginas():
    entrada = input("Digite os números das páginas separados por vírgula (ex: 23,5,12): ")
    paginas = [int(pg.strip()) for pg in entrada.split(',')] 
    return paginas

with open(pdf_file_path, 'rb') as pdf_file:
    pdf = PyPDF2.PdfReader(pdf_file)

    total_paginas = len(pdf.pages)
    print(f"Número de páginas: {total_paginas}")

    paginas_selecionadas = selecionar_paginas()

    extrair_texto_paginas(pdf, paginas_selecionadas)